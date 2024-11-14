#from crypt import methods
from flask import Flask, jsonify, request
from configparser import ConfigParser
import psycopg2

import sys
import os
import os.path
import time

api = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    options="-c timezone=Europe/Rome")

@api.route('/login', methods=['POST'])
def login():
    
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            
            jsonReq = request.json
            id = jsonReq.get('id_utente')
            pwd = jsonReq.get('pwd_utente')
            
            cur = conn.cursor()
            if cur is None:
                return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
            query=("SELECT id,password from operatori where id = %s and password = %s")
            cur.execute(query, (id, pwd))
            result = cur.fetchone()
            operatore={"id":id,"password":pwd}
            if result:
                query = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW() AT TIME ZONE 'Europe/Rome', %s , %s);"
                cur.execute(query, (id,"Login"))
                conn.commit()
                print("Operazione inserita con successo.")
                return jsonify({"Esito": "200", "Msg": "Dati corretti","operatore":operatore}), 200
            else:
                return jsonify({"Esito": "403", "Msg": "ID errato"}), 403
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        if cur is not None:
            cur.close()

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            
            jsonReq = request.json
            nome = jsonReq.get('nome')
            cognome = jsonReq.get('cognome')
            cf = jsonReq.get('cf')
            op = jsonReq.get("operatore")
            id = op.get("id")
            if not nome or not cognome or not cf:
                return jsonify({"Esito": "400", "Msg": "Dati mancanti"}), 400
            
        if int(id) == 1:
            cur = conn.cursor()
            if cur is None:
                return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
            query="INSERT INTO cittadini (nome, cognome, codice_fiscale) VALUES (%s, %s, %s);"
            cur.execute(query, (nome,cognome,cf))
            conn.commit()
            if cur.rowcount > 0:
                query = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s , %s);"
                cur.execute(query, (id,"Add cittadino"))
                conn.commit()
                return jsonify({"Esito": "200", "Msg": "Cittadino inserito","operatore":op}), 200
            else:
                return jsonify({"Esito": "403", "Msg": "Cittadino non inserito"}), 403
        else:
            return jsonify({"Esito": "403", "Msg": "Operatore non ha i permessi"}), 403
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        # Chiusura del cursore e della connessione
        if cur is not None:
            cur.close()

@api.route('/read_cittadino', methods=['POST'])
def read_cittadino():
    
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            cf = jsonReq.get('codFiscale')
            op = jsonReq.get("operatore")
            id = op.get("id")
        
            cur = conn.cursor()
            if cur is None:
                return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
            query=("SELECT * from cittadini where codice_fiscale = %s")
            cur.execute(query, (cf,))
            result = cur.fetchone()
            print(result)
            if result:
                query = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s , %s);"
                cur.execute(query, (id,"Cerca cittadino"))
                conn.commit()
                return jsonify({"Esito": "200", "Msg": "Cittadino trovato","operatore":op,"cittadino":result}), 200
            else:
                return jsonify({"Esito": "403", "Msg": "cittadino non trovato"}), 404
        
    except Exception as e:
        print(f"Errore: {e}")  # Stampa l'errore nel terminale
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        # Chiusura del cursore e della connessione
        if cur is not None:
            cur.close()
        
@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():

    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            nome = jsonReq.get('nome')
            cognome = jsonReq.get('cognome')
            cf = jsonReq.get('cf')
            nuovo_nome = jsonReq.get('nuovo_nome')
            nuovo_cognome = jsonReq.get('nuovo_cognome')
            nuovo_cf = jsonReq.get('nuovo_cf')
            op = jsonReq.get("operatore")
            id = op.get("id")
            
            if not nome or not cognome or not cf:
                return jsonify({"Esito": "400", "Msg": "Dati mancanti"}), 400
            if int(id) == 1:
                cur = conn.cursor()
                if cur is None:
                    return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
                query="UPDATE cittadini SET nome = %s, cognome = %s, codice_fiscale = %s WHERE nome = %s AND cognome = %s AND codice_fiscale = %s;"
                cur.execute(query, (nuovo_nome, nuovo_cognome, nuovo_cf, nome, cognome, cf)) 
                rows_affected = cur.rowcount
                if rows_affected > 0:
                    query_op = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s, %s);"
                    cur.execute(query_op, (id, "Modifica cittadino"))
                    conn.commit()
                    return jsonify({"Esito": "200", "Msg": "Cittadino modificato","operatore":op}), 200
                else:
                    return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
            else:
                return jsonify({"Esito": "400", "Msg": "Richiesta non valida"}), 400
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        # Chiusura del cursore e della connessione
        if cur is not None:
            cur.close()

@api.route('/elimina', methods=['DELETE'])
def elimina_cittadino():

    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            cf = jsonReq.get('codFiscale')
            op = jsonReq.get("operatore")
            id = op.get("id")

            if int(id) == 1:
                cur = conn.cursor()
                if cur is None:
                    return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
                query_check = "SELECT * FROM cittadini WHERE codice_fiscale = %s;"
                cur.execute(query_check, (cf,))
                if cur.fetchone() is None:
                    return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
                query = "DELETE FROM cittadini WHERE codice_fiscale = %s;"
                cur.execute(query, (cf,))
                conn.commit()
                if cur.rowcount > 0:
                    query_op = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s, %s);"
                    cur.execute(query_op, (id, "Elimina cittadino"))
                    conn.commit()
                    return jsonify({"Esito": "200", "Msg": "Cittadino eliminato","operatore":op}), 200
                else:
                    return jsonify({"Esito": "403", "Msg": "Cittadino non trovato"}), 404
            else:
                return jsonify({"Esito": "400", "Msg": "Richiesta non valida"}), 400
    except Exception as e:
        print(f"Errore: {e}")
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        if cur is not None:
            cur.close()

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc")