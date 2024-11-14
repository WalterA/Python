import sys
import os
import os.path
import time

#pip3 install psycopg2-binary
import dbclient as db


print("Inizio programma prova database")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()


sQuery = "INSERT INTO cittadini (nome, cognome, data_di_nascita, codice_fiscale, password) VALUES ('M', 'R','25/', 'RSS43A85M15H501Z','re');"
db.write_in_db(cur,sQuery)

sQuery = "select * from cittadini limit 5;"
iNumRows = db.read_in_db(cur,sQuery)
for ii in range(0,iNumRows):
	ok, myrow = db.read_next_row(cur)
	if ok:
		print(myrow)
 
	if 'RSS43A85M15H501Z' in myrow:
		print(True)
	