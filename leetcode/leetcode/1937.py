


bloccatooo
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        indice_lista = 1
        indice_riga = 0
        lista=[]
        tot = 0
        tempMax = 0
        for i in points:
            
            tempMax=max(i)
            tot += tempMax
            if len(lista) == 2:
                break
            else:
                index = i.index(tempMax)
                lista.append(index)
        
        x=abs(lista[0])
        y=abs(lista[1])
        sub = x-y+1
        return tot - sub
                
            
        
points = [[1,5],[3,2],[4,2]]
sol=Solution()
print(sol.maxPoints(points))