def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
    # Scrivi una funzione che prenda un dizionario e un valore, e ritorni una lista
    # con tutte le chiavi che corrispondono a quel valore,
    # o una lista vuota se il valore non è presente
    chiavi_con_valore = []
    for chiave, valore_chiave in dizionario.items():
        if valore_chiave == valore:
            chiavi_con_valore.append(chiave)
        
    return chiavi_con_valore