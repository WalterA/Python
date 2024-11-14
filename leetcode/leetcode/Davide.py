"""Dato un array e un numero intero, crea una una lista con la lunghezza n contenente i primi numeri pari del array,
stesso discorso per i dispari, dopo conta quanti numeri sono superiori a n in entrambbe le liste 
NOTA BENE : SONO VIETATI I FOR """
def dinamicopuoi(lista: list[int],n:int): #return list[int], list[int],int
    index_partenza=0
    sottolistadispari=[]
    sottolistapari=[]
    conta=0
    #temp=0 da usare dopo alcune cose
    while conta != n:
        if lista[index_partenza] % 2 == 0:
            sottolistapari.append(lista[index_partenza])
            lista.pop(index_partenza)
            conta+=1
        else:
            
            index_partenza +=1
    index_partenza = 0
    conta = 0
    while conta != n:
        if lista[index_partenza] % 2 != 0:
            sottolistadispari.append(lista[index_partenza])
            lista.pop(index_partenza)
            conta+=1
        else:
            index_partenza +=1
    conta = 0
    index_partenza =0
    while index_partenza != len(sottolistadispari):
        if sottolistadispari[index_partenza] > n:
            conta+=1
            index_partenza+=1
        else:
            index_partenza+=1
    temp=conta
    conta=0
    index_partenza=0
    while index_partenza != len(sottolistapari):
        if sottolistapari[index_partenza] > n:
            conta+=1
            index_partenza+=1
        else:
            index_partenza +=1
    result = temp+conta
    return sottolistapari, sottolistadispari , result

n=[2,3,4,5,6,7,8]
a=2
print(dinamicopuoi(n,a))
    
#([2, 4], [3, 5], 3)
"""consiglio 1
riparti da 0 usando tanti while"""