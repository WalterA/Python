import requests, json
import sys

base_url = "https://127.0.0.1:8080"
id_utente = ""
pwd_utente = ""

def GetDatiCittadino():
    id = input("Inserisci ID operatore: ")
    passw = input("Inserisci Password dell'operatore: ")
    nome = input("Qual è il nome? ")
    cognome = input("Qual è il cognome? ")
    dataN = input("Qual è la data di nascita? ")
    codF = input("Qual è il codice fiscale? ")

    datiCittadino = {"nome": nome, "cognome": cognome, "data nascita": dataN, "codice fiscale": codF, "ID": id, "Password": passw}
    return datiCittadino  # Modificato per includere ID e Password nel dizionario finale

def GetFi():
    id = input("Inserisci ID operatore: ")
    passw = input("Inserisci Password dell'operatore: ")
    codF = input("Qual è il codice fiscale? ")
    fi = {"ID": id, "Password": passw, "codice fiscale": codF}  # Corretto il campo 'password' in 'Password'
    return fi

def operatore(codop: str):
    passop = input("Inserisci la password: ")
    operatore = {"ID": codop, "Password": passop}
    return operatore

access = True
while access:
    print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
    codop = input("Inserisci il codice: ")
    
    if codop:
        api_url = base_url + "/operatore"
        jsonDataRequest = operatore(codop)
        try:
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            if data1["Esito"] == "000":
                id_utente = data1["ID"]
                pwd_utente = data1["Password"]
                adim = data1["operatore"]
                print(data1)
            else:
                print("Operatore non trovato")
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    
    if adim == "true":
        if data1["Msg"] == "Buon lavoro":
            print("Operazioni disponibili:")
            print("1. Inserisci cittadino (es. atto di nascita)")
            print("2. Richiedi cittadino (es. cert. residenza)")
            print("3. Modifica cittadino (es. cambio residenza)")
            print("4. Elimina cittadino (es. trasferim altro comune)")
            print("5. Termina lavoro")
            sOper = input("Cosa vuoi fare? ")
        else:
            print("Dati errati, riprovare")
        
        if sOper == "1":
            print("Richiesto nuovo cittadino")
            api_url = base_url + "/add_cittadino"
            jsonDataRequest = GetDatiCittadino()
            try:
                response = requests.post(api_url, json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                if data1["Esito"] == "000":
                    if data1["ID"] == id_utente and data1["Password"] == pwd_utente:
                        print("Cittadino inserito con successo")
                        print(data1)
                    else:
                        print("Dati errati")      
                else:
                    print("Dati errati")      
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        
        if sOper == "2":
            print("Richiesto codice fiscale cittadino")
            api_url = base_url + "/cerca_cittadino"
            jsonDataRequest = GetFi()
            try:
                response = requests.get(api_url, json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                if data1["Esito"] == "000":
                    if data1["ID"] == id_utente and data1["Password"] == pwd_utente:
                        print(data1["Cittadino"])
                    else:
                        print("Dati errati")      
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        if sOper == "3":
            print("Richiesto atto di nascita")
            api_url = base_url + "/modifica"
            jsonDataRequest = GetDatiCittadino()
            try:
                response = requests.put(api_url, json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                if data1["Esito"] == "000":
                    id_utente = jsonDataRequest["ID"]
                    pwd_utente = jsonDataRequest["Password"]
                    print(data1)
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        if sOper == "4":
            print("Richiesto atto di nascita")
            api_url = base_url + "/elimina"
            jsonDataRequest = GetFi()
            try:
                response = requests.delete(api_url, json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                if data1["Esito"] == "000":
                    id_utente = jsonDataRequest["ID"]
                    pwd_utente = jsonDataRequest["Password"]
                    print(data1)
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        if sOper == "5":
            print("Fine lavoro")
            access = False
            sys.exit()

    else:
        if data1["Msg"] == "Buon lavoro":
            print("Richiedi cittadino (es. cert. residenza)")
            print("Richiesto codice fiscale cittadino")
            api_url = base_url + "/cerca_cittadino"
            jsonDataRequest = GetFi()
            try:
                response = requests.get(api_url, json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                if data1["Esito"] == "000":
                    id_utente = jsonDataRequest["ID"]
                    pwd_utente = jsonDataRequest["Password"]
                    print(data1)
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")

    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci")
    sOper = input("Cosa vuoi fare? ")
