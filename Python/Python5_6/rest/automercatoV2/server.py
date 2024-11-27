import sys
from flask import Flask, app, json, request, render_template , redirect, url_for
import Python.Python5_6.rest.automercatoV2.funzioni.dbclient as db



app = Flask(__name__)

# 1. API per aggiungere un veicolo (automobili o motociclette)
@app.route('/addVeicolo', methods=['POST'])
def add_veicolo():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            data = request.get_json()
            tabella = data['tabella']
            modello = data['modello']
            filiale_id = data['Filiale']

            if tabella not in ['automobili', 'motociclette']:
                return {"Messaggio": "Tipo veicolo non valido"}
            if tabella == "automobili":
                sql_insert = f"INSERT INTO automobili (modello, magazzino) VALUES ('{modello}', {filiale_id});"
            elif tabella == "motociclette":
                sql_insert = f"INSERT INTO motociclette (modello, magazzino) VALUES ('{modello}', {filiale_id});"
            
            result = db.write_in_db(mydb, sql_insert)

            if result == 0:
                return {"Messaggio": "Veicolo aggiunto con successo!"}
            else:
                return {"Messaggio": "Errore durante l'inserimento del veicolo"}
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
        finally:
            db.close(mydb)
    else:
        db.close(mydb)
        return {'Esito': 'errore', 'Messaggio': 'Content-Type non supportato'}


# 2. API per verificare se una filiale esiste
@app.route('/verificaFiliale', methods=['GET'])
def verifica_filiale():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    try:    
        nome = request.args.get('nome')

        sql_select = f"SELECT id FROM filiale WHERE nome = '{nome}';"
        result = db.read_in_db(mydb, sql_select)
        if result > 0:
            return {"filiale_esistente": True}
        else:
            return {"filiale_esistente": False}
    except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
    finally:
        db.close(mydb)

# 3. API per ottenere l'ID di una filiale
@app.route('/getFilialeId', methods=['GET'])
def get_filiale_id():
    mydb = db.connect()
    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    else:
        print("Connessione al DB riuscita")
    try:   
        nome = request.args.get('nome')

        sql_select = f"SELECT id FROM filiale WHERE nome = '{nome}';"
        result = db.read_in_db(mydb, sql_select)

        if result > 0:
            
            row = db.read_next_row(mydb)
            
            return {"id": row['id']}
        else:
            
            return {"Messaggio": "Filiale non trovata"}
    except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return {'Esito': 'errore', 'Messaggio': 'Errore durante l\'inserimento'}
    finally:
        db.close(mydb)
