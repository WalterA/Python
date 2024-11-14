def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    """Scrivi una funzione che accetti un dizionario di prodotti con i relativi 
    prezzi e restituisca un nuovo dizionario 
    con solo i prodotti che
    hanno un prezzo inferiore a 50, ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali."""
    diz:dict={}
    for k,v in prodotti.items():
        
        if v < 50:
            temp =v+(v * 10 /100)
            temp = round(temp, 2)
            diz[k]=temp
            
    return diz
print(filtra_e_mappa({"prodotto1": 50.0, "prodotto2": 49.99, "prodotto3": 25.0}))