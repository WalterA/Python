class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        lista1=[]
        lista= list(zip(names,heights))
        lista.sort(key=lambda x:x[1])
        lista.reverse()
        for n,h in lista:
            lista1.append(n)
        return lista1
names =["Alice","Bob","Bob"]
heights = [155,185,150]
#Output: ["Bob","Alice","Bob"]
sol=Solution()
print(sol.sortPeople(names,heights))
            