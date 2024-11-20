from myjson import *

def Operatore():
    id = input("Inserisci id: ")
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    filiale = input("Inserisci la tua filiale: ").capitalize()
    return {"Id": id , "Username":username ,"Password" : password,"Filiale":filiale}

def RegistraOperatore (sFile):
    id = input("Inserisci id? ")
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    filiale = input("Inserisci la tua filiale: ").capitalize()
    risultato =  JsonSerializeAppend({"Id":id,"Username":username,"Password":password,"Filiale": filiale},sFile)
    if risultato == 0:
        return "Inserito con successo"
    else:
        return "Qualcosa è andato storto "+str(risultato)

