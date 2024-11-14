"""Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi."""
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    diz: dict[str:list[int]]={"positivi":[],"negativi":[]}  
    for i in lista:
        if i > 0:
            diz["positivi"].append(i)
        else:
            diz["negativi"].append(i)
    return diz
print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))