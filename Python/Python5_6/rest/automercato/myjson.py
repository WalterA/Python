import json
import os

def JsonSerializeAppend(dData, sFile) -> int:
    if type(dData) is not dict:
        return 1  # Ritorna 1 se i dati non sono un dizionario
    try:
        # Controlla se il file esiste e leggilo
        if os.path.exists(sFile):
            with open(sFile, "r") as read_file:
                existing_data = json.load(read_file)
            # Assicurati che il contenuto sia un dizionario
            if type(existing_data) is dict:
                # Controlla se l'ID esiste già nel dizionario
                if dData["Id"] in existing_data:
                    print(f"Operatore con ID {dData['Id']} già esistente.")
                    return -1  # Ritorna -1 se l'ID esiste già
                else:
                    existing_data[dData["Id"]] = dData  # Aggiungi il nuovo operatore al dizionario
            else:
                return 3  # Errore: il contenuto esistente non è un dizionario
        else:
            # Se il file non esiste, inizializza un nuovo dizionario con l'ID come chiave
            existing_data = {dData["Id"]: dData}

        # Scrivi i dati aggiornati nel file
        with open(sFile, "w") as write_file:
            json.dump(existing_data, write_file, indent=4)
        return 0  # Successo

    except Exception as e:
        print(f"Errore durante l'aggiornamento del file JSON: {e}")
        return 2  # Errore generico
#Serializzare 
def JsonSerialize(dData, sFile)->int:
    if type(dData) is not dict:
        return 1
    try:
        with open(sFile, "w") as write_file:
            json.dump(dData, write_file,indent=4)
        return 0
    except:
        return 2

def JsonDeserialize(sFile)->dict:
    with open(sFile, "r") as read_file:
        return json.load(read_file)
