from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys
from datetime import datetime

api = Flask(__name__)
    
@api.route('/ControllaVendite',methods=['GET'])
def Controlla():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
        
    
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        try:
            inizio= request.json.get('inizio')
            fine = request.json.get('fine')
            sQuery=f"select * from vendite where data_vendita between '{inizio}' and '{fine}';"
            iRetValue = db.read_in_db(mydb, sQuery)
            if iRetValue > 0:
                sValue = db.read_next_row(mydb)
                print(sValue)
                return {'Esito': 'ok', "dati": sValue}
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
                
    
@api.route('/Compra', methods=['PATCH'])
def Compra():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        try:
            modello = request.json[1]
            filiale = request.json[2]
            scelta = request.json[0]
            sQuery = f"update {scelta} set disponibile = false where modello = '{modello}' and magazzino = '{filiale}'"
            
            iRetValue = db.write_in_db(mydb, sQuery)
            if iRetValue == 0:
                today_date = datetime.now().strftime('%Y-%m-%d')
                insert_query = f"INSERT INTO vendite (filiale, tipo, data_vendita) VALUES ('{filiale}', '{scelta}', '{today_date}')"
                db.write_in_db(mydb, insert_query)
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

@api.route('/CercaMotocicletta', methods=['GET'])
def controlloMotocicletta():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        try:
            modello = request.json.get('modello')
            filiale = request.json.get('Filiale')
            print(f"{modello}+{filiale}")
            sQuery = f"select * from motociclette where modello = '{modello}' and magazzino = '{filiale}' and disponibile = true"
            print(sQuery)
            iRetValue = db.read_in_db(mydb, sQuery)
            print(iRetValue)
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                print(sValue)
                return {'Esito': 'ok', "dati": sValue}
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

    
@api.route('/CercaAutomobile', methods=['GET'])
def controlloAuto():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        try:
            modello = request.json.get('modello')
            filiale = request.json.get('Filiale')
            print(modello, filiale)
            # Query per cercare l'automobile disponibile
            sQuery = f"select * from automobili where modello = '{modello}' and magazzino = '{filiale}' and disponibile = true"
            
            # Leggi i dati dal DB
            iRetValue = db.read_in_db(mydb, sQuery)
            print(iRetValue)
            
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                print(sValue)
                return {'Esito': 'ok', "dati": sValue}
            else:
                return {'Esito': 'errore', 'Messaggio': 'Nessun risultato trovato'}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore nella richiesta'}
        finally:
            db.close(mydb)
    else:
        db.close(mydb)
        return 'Content-Type not supported!'



@api.route('/addop', methods=['PATCH'])
def addop():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
        
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            dati = request.json
            filiale= dati.get("Filiale")
            id = dati.get("Id") 
            if not filiale or not id:
                return {'Esito': 'errore', 'Messaggio': 'Parametri mancanti'}
            sQueryCheck = f"SELECT id FROM filiale WHERE filiale = '{filiale}'"
            fil = db.read_in_db(mydb, sQueryCheck)
            if fil>0:
                sQueryCheck = f"SELECT id FROM filiale WHERE id = '{id}'"
                id1=db.read_in_db(mydb,sQueryCheck)
                if id1 == 0:
                    sQueryUpdate = f"INSERT INTO filiale (id, filiale) VALUES ('{id}', '{filiale}');"
                    res=db.write_in_db(mydb, sQueryUpdate)
                    if res ==0:
                        return {'Esito': 'ok', 'Messaggio': 'Nuovo ID aggiunto alla filiale esistente'}
                    else:
                        return {'Esito': 'Errore'}
                else:
                    return (id + "Esistente")
            else:
                return {'Esito': 'errore', 'Messaggio': 'Non esiste la filiale'}, 500
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore nella richiesta'}, 500
        finally:
            db.close(mydb)
    else:
        db.close(mydb)
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}, 415

@api.route('/controllo_filiera', methods=['GET'])
def controlloOP():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    content_type = request.headers.get('Content-Type')
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