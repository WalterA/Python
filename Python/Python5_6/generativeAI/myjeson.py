import sys, json
path='ITSCloud-main/Python/Python5_6/json/esempio.json' #Assegna il percorso del file esempio.json alla variabile path.
thisdict={"brend":"ford",
          "electric":False,
          "year":1964,
          "colors":["red", "white", "blue"]}
thisdict2 = "{\"brand\":\"ford\",\"electric\":false,\"year\":1964,\"colors\":[\"red\", \"white\", \"blue\"]}"#Crea una stringa JSON chiamata thisdict2 che rappresenta lo stesso dizionario di thisdict, ma in formato JSON.

def Serializza(thisdict, path):
    str=json.dumps(thisdict) #Converte il dizionario thisdict in una stringa JSON utilizzando la funzione json.dumps e assegna il risultato alla variabile str.
    try:
        """Tenta di aprire il file specificato dal percorso path in modalità scrittura ('w').
        Se l'operazione riesce,
        scrive la stringa JSON str nel file e restituisce True."""
        with open(path,'w') as f:
            f.write(str)            
        return True
    except Exception as e:
        return False

def Deserializza(path):
    try:
        """Tenta di aprire il file specificato dal percorso path in modalità lettura ('r').
        Se l'operazione riesce, legge il contenuto del file e lo converte in un dizionario
        Python utilizzando la funzione json.load.
        Restituisce il dizionario."""
        with open(path,'r') as f:
            
            return json.load(f)
    
    except Exception as e:
        return None

print(Serializza(thisdict,path))
print(Deserializza(path))