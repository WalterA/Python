class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        lista = []
        temp = []
        conta = 0
        if m ==1 and n == 1 and len(original) !=1:
            return []
        for i in original:
            if conta == n:
                lista.append(temp)
                temp = []
                conta = 0
                temp.append(i)
                conta += 1
            else:
                temp.append(i)
                conta += 1
        lista.append(temp)
        if len(lista) != m:
            return []
            
        for i in lista:
            if len(i) != n:
                    return []
            
        return lista
                    
            

original = [2]
m = 1
n = 1
sol=Solution()
print(sol.construct2DArray(original,m,n))
