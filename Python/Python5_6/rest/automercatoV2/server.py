from flask import Flask, app, json, request, render_template , redirect, url_for
import random
import os
import dbc as db
import sys
from datetime import datetime

"""GENERICHE"""
def Connessione():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
        return mydb
    
def ControlloHeaders(mydb):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return True
    else:
        db.close(mydb)
        return False
"""FINE GENERICHE"""

api = Flask(__name__)

@api.route("/CercaVeicolo", methods=['GET'])
def Cerca():
    mydb = Connessione()
    if ControlloHeaders(mydb):
        try:
            dati = request.json
            print(dati)
            tabella = dati.get("tabella")
            marca = dati.get("marca")
            filiale = dati.get("filiale")
            insert_query = f"SELECT a.id, a.tipo, a.descrizione, f.marca, f.filiale, f.disponibile FROM {tabella} a JOIN accessori f ON a.id = f.id_accessori WHERE a.id IN (SELECT id FROM {tabella} WHERE marca = '{marca}' AND disponibile = True AND filiale = '{filiale}');"
            esito = db.read_in_db(mydb,insert_query)
            print(esito)
            if esito > 0:
                valori = db.read_next_row(mydb)
                print(valori)
                return {"dati":valori}
            else:
                return {'Esito': 'Dati non trovati'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
        finally:
            db.close(mydb)
    else:
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}
                    

                
@api.route('/addVeicolo', methods=['POST'])
def Addveicolo():
    mydb = Connessione()
    if ControlloHeaders(mydb):
        try:
            dati = request.json
            tabella = dati.get('tabella')
            marca = dati.get("marca")
            filiale = dati.get("filiale")
            accessori = dati.get('accessori')
            bool = dati.get('Bool')
            insert_query = f"INSERT INTO {tabella} (marca, filiale, id_accessori, disponibile) VALUES ( '{marca}', '{filiale}',{accessori},{bool});"
            esito = db.write_in_db(mydb, insert_query)
            if esito == 0:
                return {'Esito': 'ok', 'Messaggio': 'Veicolo aggiunto correttamente',"veicolo":[tabella,marca,filiale,accessori,bool]}
            else:
                return {'Esito': 'errore', 'Messaggio': 'Inserimento fallito'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
        finally:
            db.close(mydb)
    else:
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}
    

@api.route('/addop', methods=['PATCH'])
def addop():
    mydb = Connessione()
    if ControlloHeaders(mydb):
        try:
            dati = request.json
            filiale = dati.get("filiale")
            if not id or not filiale:
                return {'Esito': 'errore', 'Messaggio': 'Parametri mancanti'}
            
            sQueryUpdate = f"INSERT INTO operatori (id_filiale) VALUES ((SELECT id FROM filiale WHERE nome = '{filiale}' LIMIT 1));"
            res=db.write_in_db(mydb, sQueryUpdate)
            if res ==0:
                return {'Esito': 'ok', 'Messaggio': 'Nuovo ID aggiunto alla filiale esistente'}
            else:
                return {'Esito': 'Errore'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
        finally:
            db.close(mydb)
    else:
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}


    
api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   