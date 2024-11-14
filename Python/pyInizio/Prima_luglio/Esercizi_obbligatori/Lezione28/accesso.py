def verifica_accesso(user: str, passw: str, stato: bool) -> str:
    # L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a
    # "67890" e l'account è attivo (True). La funzione ritorna "Ingresso consentito" 
    # oppure "Ingresso negato"
    if user == "manager" and passw == "67890" and stato is True:
        return "Ingresso consentito"
    else:
        return "Ingresso negato"