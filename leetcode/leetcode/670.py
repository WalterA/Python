class Solution:
    def maximumSwap(self, num: int) -> int:
        
        st = str(num)
        lista = []

        # Converti ogni cifra in intero e aggiungi alla lista
        for i in st:
            lista.append(int(i))

        # Trova il massimo e il suo indice
        massimo = max(lista)
        indexM = lista.index(massimo)

        # Se il primo elemento è minore del massimo trovato, esegui lo scambio
        if lista[0] < lista[indexM]:
            lista[0], lista[indexM] = lista[indexM], lista[0]
        
        # Ritorna il numero come intero
        return int(''.join(map(str, lista)))

        
                
s=Solution()
print(s.maximumSwap(2736)) # 7236
                
    
            