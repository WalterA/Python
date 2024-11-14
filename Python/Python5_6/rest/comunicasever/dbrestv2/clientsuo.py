import requests
import sys
import threading

# Funzione per terminare il programma dopo 10 secondi di inattività
def timeout():
    print("Tempo scaduto. Uscita dal pr ogramma.")
    sys.exit()

# Imposta il timer di 10 secondi
timer = threading.Timer(10, timeout)

# Funzione per resetare il timer
def reset_timer():
    global timer
    timer.cancel()  # Cancella il timer attuale
    timer = threading.Timer(5000, timeout)  # Imposta un nuovo timer
    timer.start()  # Avvia il timer

id_utente = ""
pwd_utente = ""
base_url = "https://127.0.0.1:8080"
operatore= None

def GetDatiCittadino():
    nome = input("Qual è il nome? ").capitalize()
    reset_timer() 
    cognome = input("Qual è il cognome? ").capitalize()
    reset_timer()
    codF = input("Qual è il codice fiscale? ").upper()
    reset_timer() 
    return nome , cognome , codF

def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ').upper()
    reset_timer() 
    return cod

access = False
print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
conta=3
while access == False:
    while not access:
        api_url = base_url + "/login"
        id_utente = input("Inserisci ID operatore: ")
        if conta == 1:
            print("Raggiunto il massimo di errori, arrivederci")
            access = False
            sys.exit()
        if id_utente.isdigit():
            pwd_utente = input("Inserisci Password dell'operatore: ").lower()
            jsonDataRequest = {'id_utente': id_utente, 'pwd_utente': pwd_utente}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                data1 = response.json()
                if data1.get("Esito") == "200":
                    access = True
                    operatore = data1["operatore"]
                    print(data1["Msg"])
                    reset_timer() 
                else:
                    print("Dati errati, riprova.")
            else:
                print(f"Errore nella richiesta: {response.status_code}")
        else:
            conta-=1
            print(f"ID operatore non valido. Inserisci solo numeri. Tentativi rimasti {conta}")

while access:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")
    
    reset_timer() 
    
    sOper = input("Cosa vuoi fare?")
    
    if int(operatore["id"]) > 1:
        if sOper == "2":
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = {"codFiscale" : GetCodicefiscale(),"operatore":operatore}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                response=response.json()
                cittadino = response["cittadino"]
                id_operatore = response["operatore"]["id"] 
                print(f"Cittadino: {cittadino}, ID Operatore: {id_operatore}")
            else:
                print(f"Errore nella richiesta: {response.status_code}, {response.text}")
        else:
            print("Operazione non consentita")
            
        if sOper == "5":
            print("Fine lavoro")
            access = False
            sys.exit()
    else:
        if sOper == "1":
            print("Nuovo cittadino")
            api_url = base_url + "/add_cittadino"
            nome, cognome, cf = GetDatiCittadino()
            jsonDataRequest = {"nome": nome, "cognome": cognome, "cf": cf, "operatore": operatore}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                response=response.json()
                id_operatore = response["operatore"]["id"] 
                msg=response["Msg"]
                print(f"{msg}, ID Operatore: {id_operatore}")
            else:
                print(f"Errore nella richiesta: {response.status_code}, {response.text}")
                
        elif sOper == "2":
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = {"codFiscale" : GetCodicefiscale(),"operatore":operatore}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                response=response.json()
                cittadino = response["cittadino"]
                id_operatore = response["operatore"]["id"] 
                print(f"Cittadino: {cittadino}, ID Operatore: {id_operatore}")
            else:
                print(f"Errore nella richiesta: {response.status_code}, {response.text}")
                
        elif sOper == "3":
            print("Modifica cittadino")
            api_url = base_url + '/update_cittadino'
            nome, cognome, cf = GetDatiCittadino()
            print("Inserisci i nuovi dati del cittadino")
            nuovo_nome = input("Nuovo nome: ").capitalize()
            nuovo_cognome = input("Nuovo cognome: ").capitalize()
            nuovo_cf = input("Nuovo codice fiscale: ").upper()
            
            jsonDataRequest = {
                "nome": nome, 
                "cognome": cognome, 
                "cf": cf,
                "nuovo_nome": nuovo_nome,
                "nuovo_cognome": nuovo_cognome,
                "nuovo_cf": nuovo_cf,
                "operatore": operatore
            }
            try:
                response = requests.put(api_url, json=jsonDataRequest, verify=False)
                if response.status_code == 200:
                    response=response.json()
                    id_operatore = response["operatore"]["id"] 
                    msg=response["Msg"]
                    print(f"{msg}, ID Operatore: {id_operatore}")
                else:
                    print(f"Errore nella richiesta: {response.status_code}, {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
                
        elif sOper == "4":
            print("Elimina cittadino")
            api_url = base_url + "/elimina"
            cf= GetCodicefiscale()
            jsonDataRequest = {"codFiscale": cf, "operatore": operatore}
            response = requests.delete(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                response=response.json()
                id_operatore = response["operatore"]["id"] 
                msg=response["Msg"]
                print(f"{msg}, ID Operatore: {id_operatore}")
            else:
                print(f"Errore nella richiesta: {response.status_code}, {response.text}")
        
        elif sOper == "5":
            print("Fine lavoro")
            access = False
            sys.exit()