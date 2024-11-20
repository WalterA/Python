import requests
import sys
from funzioni import *
from myjson import *

base_url = "https://127.0.0.1:8080"
sFile = r"C:\Users\nicol\OneDrive\Desktop\allrepo\Progetti\Python\Python\Python5_6\rest\automercato\operatori.json"
"""CercaAutomobile: il servizio fornisce l'elenco delle automobili che 
rispecchiano le richieste del cittadino che si rivolge alla filiale.
Ciascuna filiale è anche magazzino e quindi il rappresentante della filiale comunica 
al cittadino se l'automobile è disponibile per essere vista oppure è disponibile in un altro magazzino"""
def CercaAutomobile():
    print("Dimmi il modello dell'auto: ")
    modello = input("Modello: ")
    filiale = input("Quale Filiale ti interessa? ")
    api_url = base_url + "/CercaAutomobile"
    
    try:
        data = {"modello": modello, "Filiale":filiale}
        response = requests.get(api_url, json=data, verify=False)
        print(response.content)
        try:
            jResponse = response.json()
            if jResponse.get('Esito') == "ok":
                stato = jResponse.get('Stato', 'Stato non disponibile')
                print(f"Auto disponibile. Stato: {stato}")
            else:
                print("Auto non disponibile.")
        
        except ValueError:
            print("Errore: la risposta del server non è in formato JSON.")
        
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
    stato = None

    try:
        response = requests.get(api_url, json=operatore, verify=False)
        print(response.content)
        try:
            jResponse = response.json()
            if jResponse.get('Esito') == "ok":
                auth = True
                stato = jResponse.get('Stato', 'Stato non disponibile')
                print(f"Autenticato con successo. Stato: {stato}")
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
                    break  # Uscita dal ciclo quando l'autenticazione è riuscita
            else:
                menu1[scelta]()  # Chiamata alle altre funzioni
        else:
            print("Scelta non valida, riprova.")
    
    except Exception as e:
        print(f"Errore: {e}. Riprovare.")
        
if auth:
    try:
        menu2 = {"1":CercaAutomobile}#"2":CercaMotociclette, "3":ControllaVendite, "4" : Exit}
        scelta = input("Fai la scelta: ")
        if scelta in menu2:
            if scelta == "1":
                menu2[scelta]()
                
                if auth:
                    pass  # Uscita dal ciclo quando l'autenticazione è riuscita
            else:
                menu1[scelta]()  # Chiamata alle altre funzioni
        else:
            print("Scelta non valida, riprova.")
            
    except Exception as e:
        print(f"Errore: {e}. Riprovare.")
    
