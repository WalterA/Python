import requests,json
import sys
from myjson import *
base_url = "https://127.0.0.1:8080"
auth = False
sFile="/home/user/allrepo/Progetti/Python/Python/Python5_6/rest/Verifica/vendite.json"

def GetCasa():
    indirizzo = input("Qual'è l' inidirizzo?(con il civico) ").title()
    vani = int(input("Quanti vani? "))
    
    datiCittadino = {"indirizzo":indirizzo, "vani": vani}
    return datiCittadino
"""
def GetCittadino():
    return input("Inserisci il codice fiscale della persona richiesta: ")

def UpdateCittadino():
    dati_da_modifcare = [None for _ in range(4)]
    dati_da_modifcare[0] = input("Inserisci il codice fiscale della persona a cui vuoi modificarei i dati: ")
    nome = input("Inserisci il nome modificato (Lascia vuoto per non cambiare): ")
    cognome = input("Inserisci il cognome modificato (Lascia vuoto per non cambiare): ")
    dataN = input("Inserisci la data di nascita modificata (Lascia vuoto per non cambiare): ")
    if cognome:
        dati_da_modifcare[1] = cognome
    if dataN:
        dati_da_modifcare[2] = dataN
    if nome:
        dati_da_modifcare[3] = nome
    return dati_da_modifcare
"""
def Loginreg():
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    venditore = input("Sei un venditore? scrivi si o no: ").lower()
    if venditore == "si":
        venditore = True
    else:
        venditore = False
    return {"user": username,"pass": password, "bool": venditore}

def Login():
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    return {username: [password]}

stato = -1

while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login")
        print("2. Registrazione")
        print("3. Esci")
        login = input("Cosa vuoi fare? ")
        if login == '1':
            api_url = base_url + '/login'
            accesso = Login()
            try:
                response = requests.post(api_url,json=accesso, verify=False)
                print(response.content)
                jResponse = response.json()
                if jResponse['Esito'] == "ok":
                    auth = True
                    stato = jResponse['Stato']
                print(auth)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '2':
            api_url = base_url + '/registrazione'
            jsonDataRequest = Loginreg()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response)
                print(response.content)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '3':
            sys.exit()
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Cerca casa in vendita")
            print("2. Cerca casa in affitto")
            print("3. Cerca vendite")
            print("4. Logout")
            print("5. Esci")
            sOper = input("Cosa vuoi fare? ")
            if sOper == "1":
                print("Richiesta indirizzo e vani: ")
                api_url = base_url + "/CercaCasaVendita"
                jsonDataRequest = GetCasa()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    jResponse = response.json()
                    print(jResponse)
                    print("Vuoi comprare la casa? (scrivi si o no)")
                    if input("Risposta: ") == "si":
                        print("quale casa ti inderessa inserisci il numero iniziale.")
                        scelta = int(input("Numero: ( la prima riga è 1) "))
                        catastale = jResponse[scelta][0]
                        filiale_catastale = jResponse[scelta][8]
                        prezzo = jResponse[scelta][6]
                        filiale = int(input("Propria filiale: "))
                        jsonDataRequest = {"catastale":catastale,"filiale_catastale": filiale_catastale,"prezzo":prezzo,"filiale":filiale}
                        api_url = base_url + "/CompraCasaVendita"
                        response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                        jResponse = response.json()
                        print(jResponse)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "2":
                print("Richiesta indirizzo e vani: ")
                api_url = base_url + "/CercaCasaAffitto"
                jsonDataRequest = GetCasa()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    jResponse = response.json()
                    print("Vuoi comprare la casa? (scrivi si o no)")
                    if input("Risposta: ") == "si":
                        print("quale casa ti inderessa inserisci il numero iniziale.")
                        scelta = int(input("Numero: ( la prima riga è 1) "))
                        filiale = int(input("Propria filiale: "))
                        catastale = jResponse[scelta][0]
                        filiale_catastale = jResponse[scelta][6]
                        prezzo = jResponse[scelta][5]
                        durata = jResponse[scelta][7]
                        jsonDataRequest = {"catastale":catastale,"filiale_catastale": filiale_catastale,"filiale":filiale,"prezzo":prezzo,"durata":durata}
                        api_url = base_url + "/CompraCasaAffitto"
                        print("sto qui1")
                        response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                        print("sto qui 2")
                        jResponse = response.json()
                        print("sto qui 3")
                        print(jResponse)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "3":
                print("Dimmi da che data vuoi controllare: ")
                inizio = input("Inserisci la data di inizio (formato YYYY-MM-DD): ")
                fine = input("Inserisci la data di fine (formato YYYY-MM-DD): ")
           
                api_url = base_url + "/CercaVendita"
            
                scelta = input("1. casa in affitto\n2. casa in vendita?")
                if scelta == "1":
                    data={"inizio":inizio,"fine":fine,"casa": "affitti_casa"}
                    response = requests.post(api_url,json=[data,accesso], verify=False)
                elif scelta == "2":
                    data={"inizio":inizio,"fine":fine,"casa": "vendite_casa"}
                    response = requests.post(api_url,json=[data,accesso], verify=False)
                result = JsonSerialize(response, sFile)
                if result == 0:
                    print("Dati salvati con successo!")
                elif result == 1:
                    print("Errore: tipo di dati non valido.")
                else:
                    print("Errore durante la scrittura del file.")
                
            elif sOper == "4":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="5":
                auth = False
                print("Buona giornata!")
                sys.exit()  
