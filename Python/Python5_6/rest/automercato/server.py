from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()
    
@api.route('/CercaAutomobile', methods=['GET'])
def controlloAuto():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        try:
            modello = request.json.get('modello')
            filiale = request.json.get('Filiale')
            print(f"{modello}+{filiale}")
            sQuery = f"SELECT * FROM automobili WHERE modello = '{modello}'and magazzino = '{filiale}' and disponibile = 'true'"
            iRetValue = db.read_in_db(mydb, sQuery)
            print(iRetValue)
            if iRetValue == 1:
                return {'Esito':'ok'}
            else:
                return {'Esito': 'errore'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore nella richiesta'}
        finally:
            db.close(mydb)
    else:
        db.close(mydb)
        return 'Content-Type not supported!'



@api.route('/controllo_filiera', methods=['GET'])
def controlloOP():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        try:
            dati = request.json
            filiale= dati.get("Filiale")
            id = dati.get("Id")
            sQuery= f"select * from filiale where filiale = '{filiale}' and id = '{id}'"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue == 1:
                return {'Esito':'ok'}
            else:
                return {'Esito': 'errore'}
        except Exception as e:
            # Gestisci eventuali errori nei dati inviati
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore nella richiesta'}
        finally:
            db.close(mydb)
    else:
        db.close(mydb)
        return 'Content-Type not supported!'
        
    
    
api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   