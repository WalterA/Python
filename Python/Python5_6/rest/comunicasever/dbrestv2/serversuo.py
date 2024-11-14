#from crypt import methods
from flask import Flask, jsonify, request
from configparser import ConfigParser
import psycopg2
import dbclient as db
import sys
import os
import os.path
import time

api = Flask(__name__)

@api.route('/login', methods=['POST'])
def login():
    con = db.connect()
    if con is None:
        print("Errore connessione al DB")
        sys.exit()
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            id = jsonReq.get('id_utente')
            pwd = jsonReq.get('pwd_utente')
            query=(f"SELECT id,password from operatori where id = {id} and password = '{pwd}'")
            iNumRows = db.read_in_db(con,query)
            for ii in range(0,iNumRows):
                ok, myrow = db.read_next_row(con)
                if ok:
                    print(myrow)
                else:
                    print("Errore di ricerca, operatore non trovato")
            operatore={"id":id,"password":pwd}
            st="Login"
            if ok:
                query = f"INSERT INTO operazioni (data, operatori, op) VALUES (NOW() AT TIME ZONE 'Europe/Rome', {id} , '{st}');"
                result=db.write_in_db(con,query)
                if result == 0:
                    print("Operazione inserita con successo.")
                    return jsonify({"Esito": "200", "Msg": "Dati corretti","operatore":operatore}), 200
                elif result == -2:
                    print("Errore, operazione già presente")
                else:
                    print("Errore")
            else:
                return jsonify({"Esito": "403", "Msg": "ID errato"}), 403
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    
    finally:
        db.close(con)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    con = db.connect()
    if con is None:
        print("Errore connessione al DB")
        sys.exit()
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
            query=f"INSERT INTO cittadini (nome, cognome, codice_fiscale) VALUES ('{nome}', '{cognome}', '{cf}');"
            result = db.write_in_db(con,query)
            print(result)
            ac="Add cittadino"
            if result == 0:
                query = f"INSERT INTO operazioni (data, operatori, op) VALUES (NOW()  AT TIME ZONE 'Europe/Rome', {id} , '{ac}');"
                db.write_in_db(con,query)
                return jsonify({"Esito": "200", "Msg": "Cittadino inserito","operatore":op}), 200
            elif result == -2:
                    print("Errore, operazione già presente")
            else:
                print("Errore")
                return jsonify({"Esito": "403", "Msg": "Cittadino non inserito"}), 403
        else:
            return jsonify({"Esito": "403", "Msg": "Operatore non ha i permessi"}), 403
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        if con is not None:
            con.close()

@api.route('/read_cittadino', methods=['POST'])
def read_cittadino():
    con = db.connect()
    if con is None:
        print("Errore connessione al DB")
        return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500

    try:
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return jsonify({"Esito": "400", "Msg": "Formato non supportato"}), 400

        jsonReq = request.json
        cf = jsonReq.get('codFiscale')
        op = jsonReq.get("operatore")
        id = op.get("id") if op else None
        print (id)
        if not cf or not id:
            return jsonify({"Esito": "400", "Msg": "Dati mancanti"}), 400
        query = f"SELECT * FROM cittadini WHERE codice_fiscale = '{cf}';"
        print(f"Eseguo query: {query}")
        iNumRows = db.read_in_db(con, query)

        cittadino_data = None
        if iNumRows > 0:
            ok, myrow = db.read_next_row(con)
            if ok:
                cittadino_data = myrow
            else:
                print("Errore di ricerca, cittadino non trovato")
                return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
        else:
            return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
        ac = "Cerca cittadino"
        op_query = f"INSERT INTO operazioni (data, operatori, op) VALUES (NOW()  AT TIME ZONE 'Europe/Rome', {id}, '{ac}');"
        print(f"Eseguo query operazione: {op_query}")
        write_result = db.write_in_db(con, op_query)
        if write_result == 0:
            print("Operazione inserita con successo.")
            return jsonify({
                "Esito": "200",
                "Msg": "Cittadino trovato",
                "operatore": {"id": id},
                "cittadino": cittadino_data
            }), 200
            
        elif write_result == -2:
            print("Errore, operazione già presente")
            return jsonify({"Esito": "409", "Msg": "Operazione già registrata"}), 409
        else:
            print("Errore durante l'inserimento dell'operazione")
            return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500

    except Exception as e:
        print(f"Errore: {e}")
        return jsonify({"Esito": "500", "Msg": f"Errore interno del server: {e}"}), 500
    finally:
        if con is not None:
            con.close()

@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    con = db.connect()
    if con is None:
        print("Errore connessione al DB")
        sys.exit()
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
                query=f"UPDATE cittadini SET nome = '{nuovo_nome}', cognome = '{nuovo_cognome}', codice_fiscale = '{nuovo_cf}' WHERE nome = '{nome}' AND cognome = '{cognome}' AND codice_fiscale = '{cf}';"
                result = db.write_in_db(con,query)
                ac="Modifica cittadino"
                if result == 0:
                    query = f"INSERT INTO operazioni (data, operatori, op) VALUES (NOW()  AT TIME ZONE 'Europe/Rome', {id} , '{ac}');"
                    db.write_in_db(con,query)
                    return jsonify({"Esito": "200", "Msg": "Cittadino modificato","operatore":op}), 200
                elif result == -2:
                        print("Errore, operazione già presente")
                else:
                    print("Errore")
                    return jsonify({"Esito": "403", "Msg": "Cittadino non inserito"}), 403
            else:
                return jsonify({"Esito": "403", "Msg": "Operatore non ha i permessi"}), 403
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        if con is not None:
            con.close()

@api.route('/elimina', methods=['DELETE'])
def elimina_cittadino():
    con = db.connect()
    if con is None:
        print("Errore connessione al DB")
        sys.exit()
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            cf = jsonReq.get('codFiscale')
            op = jsonReq.get("operatore")
            id = op.get("id")
            if int(id) == 1:
                query = f"DELETE FROM cittadini WHERE codice_fiscale = '{cf}';"
                result = db.write_in_db(con,query)
                ac="Elimina cittadino"
                if result == 0:
                    query = f"INSERT INTO operazioni (data, operatori, op) VALUES (NOW()  AT TIME ZONE 'Europe/Rome', {id} , '{ac}');"
                    res=db.write_in_db(con,query)
                    print(res)
                    return jsonify({"Esito": "200", "Msg": "Cittadino eliminato","operatore":op}), 200
                elif result == -2:
                        print("Errore, operazione già presente")
                else:
                    print("Errore")
                    return jsonify({"Esito": "403", "Msg": "Cittadino non inserito"}), 403
    except Exception as e:
        print(f"Errore: {e}")
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500
    finally:
        if con is not None:
            con.close()

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc")

