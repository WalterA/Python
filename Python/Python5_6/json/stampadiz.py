"""

def print_dictionary(dData,sRoot):
    for keys , values in dData.items():
        if sRoot != "":
            print("Trova chiave"+ sRoot +"."+ keys)
        else:
            print("Trova chiave "+ keys)
        if type(dData[keys]) is dict:
            
            """