import requests
import sys
from funzioni import *
from myjson import *

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
    
