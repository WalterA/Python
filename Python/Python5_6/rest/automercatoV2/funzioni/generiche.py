
import re
import sys
from flask import Flask, app, json, request, render_template , redirect, url_for
import requests
import dbclient as db

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

def Tabella():
    print("Quale veicolo?\n1 : Automobile\n2 : Motocicletta")
    n = int(input("Inserisci il numero della scelta: "))
    if n == 1:
        tabella = "automobili"
        return tabella
    elif n == 2:
        tabella = "motociclette"
        return tabella
    else:
        return False
    
def Response(api_url, data):
    response = requests.post(api_url, json=data, verify=False)
    if response.status_code == 200:
        response_data = response.json()
        
        return True , response_data
    else:
        return False
def Password():
    password = input("Inserisci la password (almeno una lettera maiuscola e un numero): ")
    if re.search(r'[A-Z]', password) and re.search(r'\d', password):
        return password ,False
    else:
        print("Errore: la password deve contenere almeno una lettera maiuscola e un numero."), True