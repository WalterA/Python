from flask import Flask, app, json, request, render_template , redirect, url_for
import random
import os
from funzioni.dbclient import db
import sys
from datetime import datetime
from funzioni.generiche import *

app = Flask(__name__)

@api.route('/addVeicolo', methods=['POST'])
def Addveicolo():
    mydb = Connessione()
    if ControlloHeaders(mydb):
        try:
            dati = request.json
            tabella = dati.get('tabella')
            modello = dati.get('modello')
            marca = dati.get("marca")
            magazzino = dati.get('magazzino')
            if tabella not in ["automobili", "motociclette"]:
                return {'Esito': 'errore', 'Messaggio': 'Tabella non valida'}
            if not id or not modello or not magazzino or not marca:
                return {'Esito': 'errore', 'Messaggio': 'Parametri mancanti'}
            
            insert_query = f"INSERT INTO {tabella} (modello,marca, magazzino) VALUES ( '{modello}', {marca}', {magazzino});"
            esito = db.write_in_db(mydb, insert_query)
            if esito == 0:
                return {'Esito': 'ok', 'Messaggio': 'Veicolo aggiunto correttamente'}
            else:
                return {'Esito': 'errore', 'Messaggio': 'Inserimento fallito'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
        finally:
            db.close(mydb)
    else:
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}


