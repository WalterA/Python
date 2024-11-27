import requests
import sys
import re
import requests
import sys
from myjson import *
from datetime import datetime


def Menu1(scelta):
    menu1 = {"1": Reg, "2": Acc, "3": Exit}
    while True:
        try:
            if scelta in menu1:
                if scelta == "2":
                    operatore, auth = menu1[scelta]()
                    print(f"Operatore: {operatore}, Autenticazione: {auth}")
                    if auth:
                        print("Autenticazione completata con successo!")
                        return auth 
                else:
                    menu1[scelta]()
            else:
                print("Scelta non valida, riprova.")
        
        except Exception as e:
            print(f"Errore: {e}. Riprovare.")

    
def Menu2(auth):        
    if auth:
        while True:
            try:
                menu2 = {"1" : Automobile,"2" : Motocicletta, "3" : ControllaVendite,"5":addVeicolo, "4" : Exit}
                print("1 : Cerca automobile.\n2 : Motocicletta.\n3 : ControllaVendite.\n5 : AggiungiVeicolo\n4 : Exit.")
                scelta = input("Fai la scelta: ")
                if scelta in menu2:
                    menu2[scelta]()
                else:
                    print("Scelta non valida, riprova.")
            except Exception as e:
                print(f"Errore: {e}. Riprovare.")
    else:
        print("Non sei autorizzato.")

base_url = "https://127.0.0.1:8080"

def verifica_filiale(filiale):
    # Query per verificare se la filiale esiste
    api_url = base_url + "/verificaFiliale"  # Supponiamo che questa API esista
    response = requests.get(api_url, params={"nome": filiale}, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data.get('filiale_esistente'):
            return True
        else:
            print(f"La filiale '{filiale}' non esiste.")
            return False
    else:
        print(f"Errore nella richiesta per la verifica della filiale: {response.status_code}")
        return False

def addVeicolo():
    api_url = base_url + "/addVeicolo"
    try:
        print("Quale veicolo?\n1 : Automobile\n2 : Motociclette")
        n = int(input("Inserisci il numero della scelta: "))
        
        if n == 1:
            tabella = "automobili"
        elif n == 2:
            tabella = "motociclette"
        else:
            print("Scelta non valida!")
            return

        # Rimuoviamo la richiesta dell'ID, il database lo genererà automaticamente
        modello = input("Inserisci Modello: ").title()
        filiale = input("Inserisci Filiale: ").capitalize()
        
        # Verifica che la filiale esista
        if not verifica_filiale(filiale):
            return

        # Recupera l'ID della filiale dal nome
        api_url_filiale = base_url + "/getFilialeId"  # Supponiamo che questa API esista
        response = requests.get(api_url_filiale, params={"nome": filiale}, verify=False)
        if response.status_code == 200:
            data = response.json()
            filiale_id = data.get('id')
        else:
            print(f"Errore nel recupero dell'ID della filiale: {response.status_code}")
            return

        # Invia i dati per aggiungere il veicolo
        data = {"tabella": tabella, "modello": modello, "Filiale": filiale_id}
        
        response = requests.post(api_url, json=data, verify=False)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data.get('Messaggio'))
        else:
            print(f"Errore HTTP: {response.status_code}")
    except ValueError:
        print("Errore: Inserisci un numero valido per la scelta")
    except Exception as e:
        print(f"Errore imprevisto: {e}")
    
    