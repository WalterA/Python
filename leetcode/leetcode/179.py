class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        uno=[]
        deci=[]
        stringa=""
        temp=""
        temp2=[]
        intero=0
        def controllo(temp,temp2,uno):
            
            for i in uno:
                if len(temp) != 2:
                    if i == 9:
                        temp+=str(i)
                    
                    elif i == 8:
                        temp+=str(i)
                    
                    elif i == 7:
                        temp+=str(i)
                    
                    elif i == 6:
                        temp+=str(i)
                    
                    elif i == 5:
                        temp+=str(i)
                    
                    elif i == 4:
                        temp+=str(i)
                    
                    elif i == 3:
                        temp+=str(i)
                    
                    elif i == 2:
                        temp+=str(i)
                    
                    elif i == 1:
                        temp+=str(i)
                    
                else:
                    temp2.append(i)
                
            return int(temp) ,temp2,
        for i in nums:
            if i >9:
                deci.append(i)
            else:
                uno.append(i)
    
        uno.sort(reverse=True)
        if len(uno) !=1:
            intero,temp2,=controllo(temp,temp2,uno)
        else:
            if len(deci)==1:
                deci.append(uno[0])
                deci.sort()
                for i in deci:
                    stringa+= str(i)
                
                return stringa
        if len(temp2) !=1 and temp2 !=[]:
            while len(temp2) !=1:
                uno=temp2
                temp2=[]
                deci.append(intero)
                temp=""
                intero,temp2=controllo(temp,temp2,uno)
        deci.append(temp2[0])
        deci.append(intero)
        deci.sort(reverse=True)
        for i in deci:
            stringa+= str(i)
        
        return stringa
        
            
s=[3,30,34,5,9]
sol=Solution()
print(sol.largestNumber(s))
