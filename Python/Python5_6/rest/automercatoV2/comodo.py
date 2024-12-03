import requests
import sys
import re
from myjson import *
from datetime import datetime
from flask import Flask, app, json, request, render_template , redirect, url_for
from generiche import *

sFile = r"/home/user/allrepo/Progetti/Python/Python/Python5_6/rest/automercatoV2/Operatori.json"
sFile1=r"C:\Users\nicol\OneDrive\Desktop\allrepo\Progetti\Python\Python\Python5_6\rest\automercato\vendite_periodo.json"
base_url = "https://127.0.0.1:8080"



def Ritorno1():
    menu1 = {"1": Reg, "2": Acc, "3": Exit}
    while True:
        try:
            print("Benvenuto, scegli cosa vuoi fare:")
            print("1 : Registra nuovo operatore.\n2 : Accedi al portale.\n3 : Aggiungi Auto/moto\n4 : Esci.")
            scelta = input("Fai la scelta: ")
            if scelta in menu1:
                if scelta == "2":
                    auth = menu1[scelta]()
                    if auth == True:
                        print("Autenticazione completata con successo!")
                        return auth
                    else:
                        print("Autentificazione fallita!")
                        return Ritorno1() 
                else:
                    menu1[scelta]()
            else:
                print("Scelta non valida, riprova.")
        
        except Exception as e:
            print(f"Errore: {e}. Riprovare.")
    
def Ritorno(auth):        
    if auth:
        while True:
            try:
                menu2 = {"1" : CercaVeicolo, "2" : ControllaVendite, "3" : addVeicolo, "4" : Exit}
                print("1 : Cerca veicolo.\n2 : ControllaVendite.\n3 : Aggiungi veicolo.\n4 : Esci.")
                scelta = input("Fai la scelta: ")
                if scelta in menu2:
                    menu2[scelta]()
                else:
                    print("Scelta non valida, riprova.")
            except Exception as e:
                print(f"Errore: {e}. Riprovare.")
    else:
        print("Non sei autorizzato.")
        

def addVeicolo():
    api_url = base_url + "/addVeicolo"
    try:
        tabella = Tabella()
        filiale = Filiale()
        accessori = Accessori()
        marca = input("Inserisci Marca: ").title()
        
        data = {"tabella": tabella, "marca":marca, "filiale": filiale,"accessori": {accessori}, "Bool": True}
        response, response_data = ResponseGet(api_url,data)
        if response:
            print(response_data.get('Messaggio'),response_data('veicolo'))
        else:
            print(f"Errore HTTP: {response.status_code}")
    except ValueError:
        print("Errore: Inserisci un numero valido per ID e scelta")
    except Exception as e:
        print(f"Errore imprevisto: {e}")

def RegistraOperatore (sFile):
    nome = input("Inserisci l'username: ").title()
    password = Password()
    filiale = Filiale()
    risultato =  JsonSerializeAppend({"Nome":nome,"Password":password,"Filiale": filiale},sFile)
    if risultato == 0:
        print(f"Aggiunto con successo: ", {nome},{filiale})
        return
    else:
        print(f"Errore: {risultato}")
        return RegistraOperatore()
        

#f
def valida_data(data_str):
    try:
        
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def ControllaVendite():
    print("Dimmi da che data vuoi controllare: ")
    inizio = input("Inserisci la data di inizio (formato YYYY-MM-DD): ")
    while not valida_data(inizio):
        print("Errore: il formato della data di inizio non è corretto. Riprova.")
        inizio = input("Inserisci la data di inizio (formato YYYY-MM-DD): ")

    fine = input("Inserisci la data di fine (formato YYYY-MM-DD): ")
    while not valida_data(fine):
        print("Errore: il formato della data di fine non è corretto. Riprova.")
        fine = input("Inserisci la data di fine (formato YYYY-MM-DD): ")
    api_url = base_url + "/ControllaVendite"
    try:
        data={"inizio":inizio,"fine":fine}
        response= requests.get(api_url,json=data,verify=False)
        if response.status_code == 200:
            data = response.json()
            if data['Esito'] == 'ok':
                print("Vendite per periodo:")
                dati_dict = {item['id']: item for item in data['dati']}
                for i in data['dati']:
                    print(i)
                result = JsonSerialize(dati_dict, sFile1)
                if result == 0:
                    print("Dati salvati con successo!")
                elif result == 1:
                    print("Errore: tipo di dati non valido.")
                else:
                    print("Errore durante la scrittura del file.")
            else:
                print("Errore:", data['Messaggio'])
        else:
            print(f"Errore nella richiesta: {response.status_code}")
    except ValueError:
            print("Errore: la risposta del server non è in formato JSON.")
        
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
    
def CercaVeicolo():
    api_url = base_url + "/CercaVeicolo"
    
    print("Quale veicolo? ")
    mezzo = Tabella()
    if mezzo == "automobili":
        print("Dimmi il marca dell'auto: ")
        marca = input("Marca: ").title()
        filiale = Filiale()
        
        data = {"tabella": mezzo, "marca": marca, "filiale": filiale}
        
        response = requests.get(api_url, json=data, verify=False)
        if response.status_code == 200:
            jResponse = response.json()
            print(f"Auto disponibile.Dati: {jResponse.get('dati')}")
        
            print("Comprare l'auto?")
            scelta=input("Scrivere si o no: ").lower()
            if scelta == "si":
                scelta="automobili"
                risultato=Compra(scelta)
                if risultato == 1:
                    print("Comprata.")
                else:
                    print("Errore.")
            else:
                while True:
                    print("1:Continua la ricerca.\n2:Exit")
                    scelta = input("Fai la scelta: ")
                    if scelta == "1":
                        return CercaVeicolo()
                    elif scelta == "2":
                        return Ritorno()
                    else:
                        print("Scelta errata, riprova.")
        else:
            print("Errore riprovare")
            return CercaVeicolo()
    elif mezzo == "motociclette":
        print("Dimmi il marca della moto: ")
        marca = input("Marca: ").title
        filiale = Filiale()
        data = {"marca": marca, "filiale": filiale}
        api_url = base_url + "/CercaVeicolo"
        response = requests.get(api_url, json=data, verify=False)
        if response.status_code == 200:
            jResponse = response.json()
            print(f"Moto disponibile.Dati: {jResponse.get('dati')}")
            
            print("Comprare la motocicletta?")
            scelta=input("Scrivere si o no: ").lower()
            if scelta == "si":
                scelta="motociclette"
                risultato=Compra(scelta)
                if risultato == 1:
                    print("Comprata.")
                else:
                    print("Errore.")
            else:
                while True:
                    print("1:Continua la ricerca.\n2:Exit")
                    scelta = input("Fai la scelta: ")
                    if scelta == "1":
                        return CercaVeicolo()
                    elif scelta == "2":
                        return Ritorno()
                    else:
                        print("Scelta errata, riprova.")
        else:
            print("Errore riprovare")
            return CercaVeicolo()
        
        
        
        
        
def Motocicletta():
    print("Dimmi il modello della Motocicletta: ")
    modello = input("Modello: ").title()
    filiale = input("Quale Filiale ti interessa? ").capitalize()
    api_url = base_url + "/CercaMotocicletta"
    
    try:
        data = {"modello": modello, "Filiale":filiale}
        response = requests.get(api_url, json=data, verify=False)
        try:
            jResponse = response.json()
            if jResponse.get('Esito') == "ok":
                print(f"Motociclietta disponibile. Dati:{jResponse.get('dati')}")
                print("Comprare la motocicletta?")
                scelta=input("Scrivere si o no: ").lower()
                if scelta == "si":
                    scelta="motociclette"
                    risultato=Compra(scelta)
                    if risultato == 1:
                        print("Comprata.")
                    else:
                        print("Errore.")
                else:
                    while True:
                        print("1:Continua la ricerca.\n2:Exit")
                        menu3={"1":Motocicletta,"2":Ritorno}
                        scelta = input("Fai la scelta: ")
                        if scelta == "1":
                            menu3[scelta]()
                        elif scelta == "2":
                            menu3[scelta](True)
                        else:
                            print("Scelta errata, riprova.")
            else:
                print("Motocicletta non disponibile.")
        except ValueError:
            print("Errore: la risposta del server non è in formato JSON.")
        
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")


def Automobile():
    print("Dimmi il modello dell'auto: ")
    modello = input("Modello: ").title()
    filiale = input("Quale Filiale ti interessa? ").capitalize()
    api_url = base_url + "/CercaAutomobile"
    
    try:
        data = {"modello": modello, "Filiale":filiale}
        response = requests.get(api_url, json=data, verify=False)
        try:
            jResponse = response.json()
            if jResponse.get('Esito') == "ok":
                print(f"Auto disponibile.Dati: {jResponse.get('dati')}")
                print("Comprare l'auto?")
                scelta=input("Scrivere si o no: ").lower()
                if scelta == "si":
                    scelta="automobili"
                    risultato=Compra(scelta, modello, filiale)
                    if risultato == 1:
                        print("Comprata.")
                    else:
                        print("Errore.")
                else:
                    while True:
                        print("1:Continua la ricerca.\n2:Exit")
                        menu3={"1":Automobile,"2":Ritorno}
                        scelta = input("Fai la scelta: ")
                        if scelta == "1":
                            menu3[scelta]()
                        elif scelta == "2":
                            menu3[scelta](True)
                        else:
                            print("Scelta errata, riprova.")
            else:
                print("Auto non disponibile.")
        except ValueError:
            print("Errore: la risposta del server non è in formato JSON.")
        
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
        
def Compra(scelta: str, modello:str, filiale:str):
    api_url = base_url + "/Compra"
    try:
        response = requests.patch(api_url, json=[scelta,modello, filiale], verify=False)
        jResponse = response.json()
        if jResponse.get('Esito') == "ok":
            return 1
        else:
            return -1
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")

    
def Reg():
    registra = RegistraOperatore(sFile)
    return

def Acc():
    auth = Operatore()
    return auth

def Exit():
    print("Uscita dal programma.")
    sys.exit()
    
    

auth=Ritorno1()

Ritorno(auth)

