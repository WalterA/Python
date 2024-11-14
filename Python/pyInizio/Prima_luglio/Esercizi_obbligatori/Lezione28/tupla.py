"""Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, somma il valore al valore già associato alla chiave."""
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    diz: dict = {}
    for lettera, valore in tuples:
        if lettera in diz:
            diz[lettera] += valore
        else:
            diz[lettera] = valore
    return diz