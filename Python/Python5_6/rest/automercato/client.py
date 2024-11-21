import requests
import sys
from funzioni import *
from myjson import *

base_url = "https://127.0.0.1:8080"
sFile = r"C:\Users\nicol\OneDrive\Desktop\allrepo\Progetti\Python\Python\Python5_6\rest\automercato\operatori.json"
def ControllaVendite():
    print("Dimmi da che data vuoi controllare: ")
    inizio = input("Inserisci la data di inizio (formato YYYY-MM-DD): ")
    fine = input("Inserisci la data di fine (formato YYYY-MM-DD): ")
    api_url = base_url + "/ControllaVendite"
    try:
        data={"inizio":inizio,"fine":fine}
        response= requests.get(api_url,json=data,verify=False)
        if response.status_code == 200:
            data = response.json()
            if data['Esito'] == 'ok':
                print("Vendite per periodo:")
                print(json.dumps(data['Dati'], indent=4))
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
                        menu3={"1":Motocicletta,"2":Exit}
                        scelta = input("Fai la scelta: ")
                        if scelta == "1" or scelta == "2":
                            menu3[scelta]()
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
                        menu3={"1":Automobile,"2":Exit}
                        scelta = input("Fai la scelta: ")
                        if scelta == "1" or scelta == "2":
                            menu3[scelta]()
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

menu1 = {"1": Reg, "2": Acc, "3": Exit}

while True:
    try:
        print("Benvenuto, scegli cosa vuoi fare:")
        print("1: Registra nuovo operatore.\n2: Accedi al portale.\n3: Esci")
        scelta = input("Fai la scelta: ")

        if scelta in menu1:
            if scelta == "2":
                operatore, auth = menu1[scelta]()
                print(f"Operatore: {operatore}, Autenticazione: {auth}")
                if auth:
                    print("Autenticazione completata con successo!")
                    break 
            else:
                menu1[scelta]()
        else:
            print("Scelta non valida, riprova.")
    
    except Exception as e:
        print(f"Errore: {e}. Riprovare.")
        
if auth:
    while True:
        try:
            menu2 = {"1":Automobile,"2":Motocicletta, "3":ControllaVendite, "4" : Exit}
            print("1: Cerca automobile\n2:Motocicletta\n4 : Exit")
            scelta = input("Fai la scelta: ")
            if scelta in menu2:
                menu2[scelta]()
            else:
                print("Scelta non valida, riprova.")
        except Exception as e:
            print(f"Errore: {e}. Riprovare.")
else:
    print("Non sei autorizzato.")
    
