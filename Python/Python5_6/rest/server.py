from flask import Flask, json, request
from myjson import JsonSerialize, JsonDeserialize
from db_postgress import dbclient
import sys
import os
import os.path
import time
from db_postgress import dbclient as db

sOperatori = "./operatori.json"
sAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/operatore',methods=['POST'])
def verop():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sId = jsonReq["ID"]
            sPass = jsonReq["Password"]
            operatori = JsonDeserialize(sOperatori)
            
            if sId in operatori:
                op = operatori[sId]
                if sPass == op["password"]:
                    adim = op["Adim"]
                    jsonResp = {"Esito": "000", "Msg": "Buon lavoro", "operatore": adim, "ID": sId, "Password": sPass}
                    return json.dumps(jsonResp), 200
                else:
                    jsonResp = {"Esito": "001", "Msg": "Dati non validi"}
                    return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Operatore non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Content-Type not supported!', 401

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        op = JsonDeserialize(sOperatori)
        sId = jsonReq["ID"]
        sPass = jsonReq["Password"]

        # Verifica che l'operatore esista
        if sId in op:
            # Verifica che il cittadino non esista già
            if sCodiceFiscale not in anagrafe:
                dNuovoCittadino = jsonReq
                anagrafe[sCodiceFiscale] = dNuovoCittadino
                JsonSerialize(anagrafe, sAnagrafe)
                jsonResp = {"Esito": "000", "Msg": "ok", "Cittadino": dNuovoCittadino, "ID": sId, "Password": sPass}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino già presente"}
                return json.dumps(jsonResp), 200  # Modificato codice di stato errato
        else:
            jsonResp = {"Esito": "001", "Msg": "Operatore non trovato"}
            return json.dumps(jsonResp), 200  # Modificato codice di stato errato
    else:
        return 'Content-Type not supported!', 401

@api.route('/cerca_cittadino', methods=['GET'])
def CercaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            """
            anagrafe = JsonDeserialize(sAnagrafe)
            op = JsonDeserialize(sOperatori)
            sId = jsonReq["ID"]
            sPass = jsonReq["Password"]"""
            
            # Verifica se l'operatore esiste
            """if sId in op:
                # Controlla se il cittadino esiste in anagrafe
                if sCodiceFiscale in anagrafe:
                    dCittadino = anagrafe[sCodiceFiscale]"""
            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                sys.exit()

            sQuery = "select * from cittadini where cittadini.codice_fiscale;"
            iNumRows = db.read_in_db(cur,sQuery)
            for ii in range(0,iNumRows):
                myrow = db.read_next_row(cur)
                print(myrow)
                jsonResp = {"Esito": "000", "Msg": "ok", "clienti" : myrow}
                return json.dumps(jsonResp), 200
            
        except Exception as e:
            return str(e), 500
    else:
        return 'Content-Type not supported!', 401

@api.route('/modifica', methods=['PUT'])
def ModificaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        
        # Verifica se il cittadino esiste
        if sCodiceFiscale in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino  # Modifica i dati del cittadino
            JsonSerialize(anagrafe, sAnagrafe)
            jsonResp = {"Esito": "000", "Msg": "ok", "Cittadino": dNuovoCittadino}
            return json.dumps(jsonResp), 200
        else:
            jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}  # Corretto messaggio di errore
            return json.dumps(jsonResp), 200
    else:
        return 'Content-Type not supported!', 401

@api.route('/elimina', methods=['DELETE'])
def eliminaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            anagrafe = JsonDeserialize(sAnagrafe)

            # Verifica se il cittadino esiste
            if sCodiceFiscale in anagrafe:
                del anagrafe[sCodiceFiscale]  # Elimina il cittadino
                JsonSerialize(anagrafe, sAnagrafe)
                jsonResp = {"Esito": "000", "Msg": "ok", "Cittadino": "eliminato"}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Content-Type not supported!', 401

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
