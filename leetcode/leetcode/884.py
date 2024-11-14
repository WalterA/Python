from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1= s1.split()
        s2= s2.split()
        lista = s1+s2
        conta=0
        temp=[]
        """
        for i in lista:
            if i in diz:
                diz[i]+=1
            else:
                diz[i]=1
        for k,v in diz.items():
            if v==1:
                temp.append(k)
        return temp
    #alternative
        conteggio_voti = Counter(lista)
        for k,v in conteggio_voti.items():
            if v==1:
                temp.append(k)
        return temp
        #alternative
        for i in lista:
            if lista.count(i)==1:
                temp.append(i)
        return temp
        """
s1 = "this apple is sweet"
s2 = "this apple is sour"

sol=Solution()
print(sol.uncommonFromSentences(s1,s2))