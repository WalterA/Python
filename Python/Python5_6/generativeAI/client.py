
import requests, json, sys
import subprocess
from myjeson import *


base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = "AIzaSyAs5ipps05JoM4G9u2xs7ZOOkYfq-MeZOw"
api_url = base_url + sGoogleApiKey

def ComponiJsonPerImmagine(sImagePath):
    subprocess.run(["rm", "./image.jpg"])
    subprocess.run(["rm", "./request.json"])
    subprocess.run(["cp", sImagePath,"./image.jpg"])
    subprocess.run(["bash", "./json.sh"])

print("Benvenuti al Comune - sede locale")

iFlag = 0
while iFlag==0:
    
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi una domanda su un'immagine")
    print("3. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if iOper == 1:
        sDomanda = input("Inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts":[{"text": sDomanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=True)
        if response.status_code == 200:
            #print(response.json())  
            ListaRisposta =response.json()["candidates"]
            for dRisposta in ListaRisposta:
                stestorisp=dRisposta['content']['parts'][0]["text"]
                print(stestorisp)
                
    elif iOper == 2:
        sImage= input("Inserisci immagine: ")
        sDomanda=input("Inserisci la domanda: ")
        ComponiJsonPerImmagine(sImage)
        jsonDataRequest= Deserializza("request.json")
        jsonDataRequest = {"contents": [{"parts":[{"text": sDomanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=True)
        if response.status_code == 200:
            print(response.json()) 
    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")
