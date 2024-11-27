from Python.Python5_6.rest.automercatoV2.funzioni.comodo import Menu1, Menu2



print("Benvenuto, scegli cosa vuoi fare:")
print("1 : Registra nuovo operatore.\n2 : Accedi al portale.\n3 : Aggiungi Auto/moto\n4 : Esci.")
scelta = input("Fai la scelta: ")
auth = Menu1(scelta)
Menu2(auth)
