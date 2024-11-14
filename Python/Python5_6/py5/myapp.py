import time
import sys
sys.stdout = open("./ file.txt", "w+")
i=1
while i <10:
    print("Infinita")
    sys.stdout.flush()
    time.sleep(2)  # Pausa di 2 secondi
    i+=1
sys.stdout.close()


