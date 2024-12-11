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
 
def controllo_privilegi_admin(user: dict):
    for key, value in user.items():
        sQuery = f"select stato from utenti where username = '{key}' and pass = '{value[0]}';"
        print(sQuery)
        iNumRecord = db.read_in_db(mydb, sQuery)
        if iNumRecord == 1:
            lRecord = db.read_next_row(mydb)
            iStato = lRecord[1][0]
            return iStato
        return False
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        iStato = -1
        for key, value in request.json.items():
            sQuery = f"select stato from utenti where username = '{key}' and pass = '{value[0]}';"
            print(sQuery)
            iNumRecord = db.read_in_db(mydb, sQuery)
            if iNumRecord == 1:
                print("Login terminato correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                print(iStato)
                return {"Esito":"ok", "Stato": iStato}
            elif iNumRecord == 0:
                print("Credenziali errate")
                return {"Esito":"ko", "Stato": iStato}
            elif iNumRecord <= -1:
                print("Dati errati")
                return {"Esito":"ko", "Stato": iStato }
            else:
                print("Attenzione: attacco in corso")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        dati= request.json
        user = dati.get("user")
        pas = dati.get("pass")
        bol = dati.get("bool")
        sQuery = f"insert into utenti(username,pass,stato,venditore) values ('{user}', '{pas}',true,{bol})"
        print(sQuery)
        iRetValue = db.write_in_db(mydb, sQuery) #restituisce 0 se è andato tutto bene, -1 errore, -2 duplicate key
        print(iRetValue)
        if iRetValue == -2:
            return "Nome utente già in uso"
        elif iRetValue == 0:
            return "Registrazione avvenuta con successo"
        else:
            return "Errore non gestito nella registrazione"   
    else:
        return 'Content-Type not supported!'
 
   
@api.route('/CercaCasaVendita', methods=['POST'])
def CercaCasaVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        print(dati)
        indirizzo = dati.get("indirizzo")
        vani = dati.get("vani")
        lista = []
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
            sQuery = f"select * from case_in_vendita where indirizzo = '{indirizzo}' and  vani = {vani}"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                print(sValue)
                return sValue
            elif iRetValue > 1 :
                for i in range(0, iRetValue):
                    sValue = db.read_next_row()
                    lista.append(sValue)
                return lista
            else :
                return "Case non trovate"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
  
@api.route('/CercaCasaAffitto', methods=['POST'])
def CercaCasaAffitto():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        print(dati)
        indirizzo = dati.get("indirizzo")
        vani = dati.get("vani")
        lista = []
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
            sQuery = f"select * from case_in_affitto where indirizzo = '{indirizzo}' and  vani = {vani}"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                print(sValue)
                return sValue
            elif iRetValue < 1 :
                for i in range(0, iRetValue):
                    sValue = db.read_next_row()
                    lista.append(sValue)
                return lista
            else :
                return "Case non trovate"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
 
@api.route('/CompraCasaVendita', methods=['POST'])
def CompaCasaVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        print(dati)
        catastale = dati.get("catastale")
        filiale_catastale = dati.get("filiale_catastale")
        prezzo = dati.get("prezzo")
        filiale = dati.get("filiale")
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
            sQuery = f"INSERT INTO vendite_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita) VALUES ('{catastale}',CURRENT_TIMESTAMP,{filiale}, {filiale_catastale}, {prezzo});"
            esito = db.write_in_db(mydb, sQuery)
            if esito == 0:
                return {'Esito': 'ok', 'Messaggio': 'Comprata'}
            else:
                return {'Esito': 'errore', 'Messaggio': 'Inserimento fallito'}
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
   
 
@api.route('/CompraCasaAffitto', methods=['POST'])
def CompraCasaAffitto():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        print("sono qui",dati)
        catastale = dati.get("catastale")
        filiale_catastale = dati.get("filiale_catastale")
        prezzo = float(dati.get("prezzo"))
        durata = dati.get("durata")
        filiale = dati.get("filiale")
        print(catastale, filiale_catastale, durata, prezzo) 
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
            sQuery = f"INSERT INTO affitti_casa (catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto,durata_contratto) VALUES ('{catastale}',CURRENT_TIMESTAMP,{filiale_catastale},{filiale}, {prezzo},{durata});"
            esito = db.write_in_db(mydb, sQuery)
            print(esito)
            if esito == 0:
                return {'Esito': 'ok', 'Messaggio': 'Comprata'}
            else:
                return {'Esito': 'errore', 'Messaggio': 'Inserimento fallito'}
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
       
 
@api.route('/CercaVendita', methods=['POST'])
def CercaVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        inizio = dati.get("inizio")
        fine = dati.get("fine")
        casa = dati.get("casa")
        if casa == "affitti_casa":
            if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
                sQuery = f"SELECT * FROM '{casa}' WHERE data_affitto  BETWEEN '{inizio}' AND '{fine}';"
                iRetValue = db.read_in_db(mydb,sQuery)
                if iRetValue == 1:
                    sValue = db.read_next_row(mydb)
                    print(sValue)
                    return sValue
        else:
            if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
                sQuery = f"SELECT * FROM '{casa}' WHERE data_vendita BETWEEN '{inizio}' AND '{fine}';"
                iRetValue = db.read_in_db(mydb,sQuery)
                if iRetValue == 1:
                    sValue = db.read_next_row(mydb)
                    print(sValue)
                    return sValue
                else:
                    return "No"
            
            else:
                return {'Esito': 'errore', 'Messaggio': 'Inserimento fallito'}
    else:
        return 'Content-Type not supported!'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   