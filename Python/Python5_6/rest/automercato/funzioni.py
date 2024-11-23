
import re
import requests
import sys
from myjson import *
from datetime import datetime
def Ritorno1():
    menu1 = {"1": Reg, "2": Acc, "3": Exit}
    while True:
        try:
            print("Benvenuto, scegli cosa vuoi fare:")
            print("1 : Registra nuovo operatore.\n2 : Accedi al portale.\n3 : Esci.")
            scelta = input("Fai la scelta: ")

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
    
def Ritorno(auth):        
    if auth:
        while True:
            try:
                menu2 = {"1" : Automobile,"2" : Motocicletta, "3" : ControllaVendite, "4" : Exit}
                print("1 : Cerca automobile.\n2 : Motocicletta.\n3 : ControllaVendite.\n4 : Exit.")
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
""" # volevo aggiungere un nuovo elemento per auto e moto ma mi son stufato

api_url = base_url + "/addVeicolo"
def addVeicolo():
    print("Quale veicolo? 1 : Automobile\n2 : Motocicletta ")
    n = input("Inserisci il numero della scela: ")
    if n == 1:
        n="automobili"
    else:
        n="motociclette"
    print("")
    data={"Id":id,"Filiale": filiale}
    response= requests.patch(api_url,json=data,verify=False)
    try:
        if response.status_code == 200:
            data = response.json()
            if data.get('Esito') == "ok":
                return data.get('Messaggio')
            else:
                return data.get('Messaggio')
        else:
            return "Qualcosa è andato storto "+str(risultato)
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
        """

def Operatore():
    while True:
        try:
            id = int(input("Inserisci id (solo numeri interi): "))
            break  
        except ValueError:
            print("Errore: l'ID deve essere un numero intero valido.")

    username = input("Inserisci l'username: ").title()

    while True:
        password = input("Inserisci la password (almeno una lettera maiuscola e un numero): ")
        # Controlla che la password abbia almeno una maiuscola e un numero
        if re.search(r'[A-Z]', password) and re.search(r'\d', password):
            break  # Esce dal ciclo se la password è valida
        else:
            print("Errore: la password deve contenere almeno una lettera maiuscola e un numero.")
    id=str(id)
    filiale = input("Inserisci la tua filiale: ").capitalize()
    return {"Id": id , "Username":username ,"Password" : password,"Filiale":filiale}

def RegistraOperatore (sFile):
    while True:
        try:
            id = int(input("Inserisci id (solo numeri interi): "))
            break 
        except ValueError:
            print("Errore: l'ID deve essere un numero intero valido.")

    username = input("Inserisci l'username: ").title()

    while True:
        password = input("Inserisci la password (almeno una lettera maiuscola e un numero): ")
        if re.search(r'[A-Z]', password) and re.search(r'\d', password):
            break
        else:
            print("Errore: la password deve contenere almeno una lettera maiuscola e un numero.")
    id=str(id)
    filiale = input("Inserisci la tua filiale: ").capitalize()
    risultato =  JsonSerializeAppend({"Id":id,"Username":username,"Password":password,"Filiale": filiale},sFile)
    if risultato == 0:
        api_url = base_url + "/addop"
        data={"Id":id,"Filiale": filiale}
        response= requests.patch(api_url,json=data,verify=False)
        try:
            if response.status_code == 200:
                data = response.json()
                if data.get('Esito') == "ok":
                    return data.get('Messaggio')
                else:
                    return data.get('Messaggio')
            else:
                return "Qualcosa è andato storto "+str(risultato)
        except Exception as e:
            print(f"Si è verificato un errore imprevisto: {e}")
            
sFile = r"C:\Users\nicol\OneDrive\Desktop\allrepo\Progetti\Python\Python\Python5_6\rest\automercato\operatori.json"
sFile1=r"C:\Users\nicol\OneDrive\Desktop\allrepo\Progetti\Python\Python\Python5_6\rest\automercato\vendite_periodo.json"

def valida_data(data_str):
    try:
        # Tenta di fare il parsing della data con il formato specificato
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
    print(f"{registra}")
    return

def Acc():
    print("Benvenuto operatore, inserisci i tuoi dati:")
    operatore = Operatore()
    api_url = base_url + "/controllo_filiera"
    auth = False
    try:
        response = requests.get(api_url, json=operatore, verify=False)
        try:
            jResponse = response.json()
            if jResponse.get('Esito') == "ok":
                auth = True
                print(f"Autenticato con successo.")
            else:
                print("Autenticazione fallita.")
        
        except ValueError:
            print("Errore: la risposta del server non è in formato JSON.")
        
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la comunicazione con il server: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")

    print(f"Autenticazione riuscita: {auth}")
    return operatore, auth

def Exit():
    print("Uscita dal programma.")
    sys.exit()
