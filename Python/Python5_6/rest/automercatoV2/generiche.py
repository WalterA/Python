
import re
import requests
from myjson import *

sFile = r"/home/user/allrepo/Progetti/Python/Python/Python5_6/rest/automercatoV2/Operatori.json"
"""GENERICHE"""


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
        print("Scelta non valida.")
        return Tabella()
    
def Filiale():
    print("Scegli la filiale disponibile: ")
    f={1:"Roma",2 : "Torino", 3 : "Milano"}
    print("1: Roma,\n2 : Torino,\n3 : Milano")
    scelta = int(input("Inserisci la scelta: "))
    if scelta in f:
        return f[scelta]
    else:
        print("Scelta non valida.")
        return Filiale()
    
def Accessori():
    print("Per:\n1 : automobile\n2 : motociclette ")
    scelta= int(input("Inserisci scelta: "))
    if scelta == 1:
        print("Scegli l'accessorio: ")
        print("1 : Kit di pulizia esterno per auto\n2 : Copertura per esterni per auto")
        scelta=int(input("Inserisci scelta : "))
        if scelta == 1:
            return 1
        elif scelta == 2:
            return 2
        else:
            print("Scelta non valida.")
            return AddAccessori()
    elif scelta == 2:
        print("Scegli l'accessorio: ")
        print("1 : Guanti da moto in pelle\n2 : Coprisedile impermeabile per moto")
        scelta=int(input("Inserisci scelta : "))
        if scelta == 1:
            return 3
        elif scelta == 2:
            return 4
        else:
            print("Scelta non valida.")
            return AddAccessori()
    else:
        print("Scelta non valida.")
        return AddAccessori()
def AddAccessori():
    print("Accessori per quale mezzo?\n1 : automobile\n2 : motociclette ")
    scelta= int(input("Inserisci scelta: "))
    if scelta == 1:
        print("Scegli l'accessorio: ")
        print("1 : Kit di pulizia esterno per auto\n2 : Copertura per esterni per auto")
        scelta=int(input("Inserisci scelta : "))
        if scelta == 1:
            return "kit_pulizia_esterno_per_auto"
        elif scelta == 2:
            return "copertura_esterna_per_auto"
        else:
            print("Scelta non valida.")
            return AddAccessori()
    elif scelta == 2:
        print("Scegli l'accessorio: ")
        print("1 : Guanti da moto in pelle\n2 : Coprisedile impermeabile per moto")
        scelta=int(input("Inserisci scelta : "))
        if scelta == 1:
            return "guanti_da_moto_in_pelle"
        elif scelta == 2:
            return "coprisedile_impermeabile_per_moto"
        else:
            print("Scelta non valida.")
            return AddAccessori()
    else:
        print("Scelta non valida.")
        return AddAccessori()
    

def ResponseGet(api_url, data):
    try:
        response = requests.get(api_url, params=data, verify=False)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return True , response_data
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
    
def ResponsePost(api_url, data):
    response = requests.post(api_url, json=data, verify=False)
    if response.status_code == 200:
        response_data = response.json()
        return True , response_data 
    else:
        return False
    
def Password():
    password = input("Inserisci la password (almeno una lettera maiuscola e un numero): ")
    if re.search(r'[A-Z]', password) and re.search(r'\d', password):
        return password
    else:
        print("Errore: la password deve contenere almeno una lettera maiuscola e un numero.")
        return Password()
    
def Operatore():
        nome = input("Inserisci l'username: ").title()
        password=Password()
        response = JsonDeserialize(sFile)
        if nome == response["Nome"]:
            if password == response["Password"]:
                print("Benvenuto, sei un operatore autorizzato.")
                auth = True
                return auth
            else:
                print("Password non corretta.")
                return Operatore()
        else:
            print("Nome utente non corretta.")
            return Operatore()

    
"""FINE GENERICHE"""