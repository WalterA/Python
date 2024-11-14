# class Solution:
#     def controllo (self, num:int, lista:list[int]):
#         j=0
#         girata = lista[::-1]
#         copy= girata.copy()
#         i=-1
#         risultato = 0
#         while num != 5:
#             if num == 10:
#                 while risultato != 5:
#                     if girata[j] ==20:
#                         if len(lista)==1:
#                             return False , lista
#                         else:
#                             j+=1
#                     else:
#                         risultato = num - girata[j]
#                         if risultato == 0 and len(lista)>1 and len(lista)<2:
#                             j+=1
#                         elif risultato == 0 and len(lista)==1:
#                             if len(lista) == 1 and lista[j] == num:
#                                 return False , lista
#                             else:
#                                 if risultato <=0:
#                                     return False ,lista
#                                 else:
#                                     if risultato <= 0:
#                                         j+=1
#                                     else:
#                                         if risultato == 5:
#                                             lista.pop(j-1)
#                                             return True , lista
#                                         else:
#                                             if risultato <5:
#                                                 return False, lista
#                         else:
#                                     if risultato <0:
#                                         return False, lista
#                                     elif len(lista) == 2 and lista[0] == 10 and lista[1] == 10:
#                                         return False , lista
#                                     elif len(lista) >=2 and risultato!= 5 :
#                                         j+=1
#                                     elif risultato <= 0:
#                                         return False , lista
#                                     else:
#                                         if risultato == 5:
#                                             lista.pop(j-1)
#                                             return True , lista
#                                         else:
#                                             if risultato <5:
#                                                 return False, lista
#             else:
#                 while risultato != 5:
#                     if risultato == 10:
#                         booleano, lista= self.controllo (risultato, lista)
#                         return booleano, lista
#                     if 10 in girata:
#                         if girata[j] == 20:
#                             j+=1
#                         elif girata[j] == 5:
#                             j+=1
#                         else:
#                             risultato = num - girata[j]
#                             if risultato == 10:
#                                 lista.pop(-(j+1))
#                                 booleano, lista= self.controllo (risultato, lista)
#                                 return booleano, lista
#                             elif risultato == 15:
#                                 risultato = num - girata[j]
#                                 lista.pop(i)
#                                 if risultato == 10:
#                                     booleano, lista= self.controllo (risultato, lista)
#                                     return booleano, lista
#                             else:
#                                 j+1
#                     else:
#                         risultato = num - girata[j]
#                         if risultato <=0:
#                             return False , lista
#                         else:
#                             lista.pop(j)
#                             if not lista:
#                                 return False , lista
        
#                             elif risultato == 15:
#                                 num = risultato
                                
#                                 j=0
#                             else:
                                
#                                 j+1
                
            
#     def lemonadeChange(self, bills: list[int]) -> bool:
#         lista=[]
#         i=0
#         j=0
#         for i in range(len(bills)):
#             if bills[i] == 5:
#                 lista.append(bills[i])
#             else:
#                 if not lista:
#                     return False
#                 else:
#                     booleano , lista = self.controllo(bills[i],lista)
#                     if booleano is True:
#                         lista.append(bills[i])
                        
#                     else:
#                         return False
                
#         return True

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cinque, dieci = 0, 0
        for i in bills:
            if i == 5:
                cinque += 1
            elif i == 10:
                if cinque == 0:
                    return False
                cinque -= 1
                dieci += 1
            else:
                if dieci > 0 and cinque > 0:
                    dieci -= 1
                    cinque -= 1
                elif cinque >= 3:
                    cinque -= 3
                else:
                    return False
        return True







bills =[5,5,5,5,5,20,5,20,5,5,5,10,20,5,5,10,5,10,5,10,5,5,5,20,10,5,5,5,5,5,5,20,5,10,10,20,5,20,5,5,10,5,20,5,5,5,10,5,10,10,10,10,10,5,20,5,20,20,5,5,5,5,5,5,5,20,10,5,5,5,20,5,5,5,20,5,5,5,5,20,20,5,5,20,20,5,5,5,20,5,5,10,10,10,5,20,20,5,20,5,5,10,10,20,20,5,5,20,10,5,5,10,20,5,20,5,5,5,20,5,20,5,5,5,5,5,5,5,20,20,10,5,5,5,5,20,5,20,20,5,10,10,20,20,20,5,5,5,5,10,10,5,5,20,20,10,5,5,10,20,5,5,5,5,5,20,10,20,5,5,5,10,5,5,5,10,5,5,10,10,20,5,5,10,10,10,10,5,5,5,5,20,10,5,20,10,5,5,5,20,10,5,5,5,5,5,5,5,10,10,10,5,20,5,5,5,5,20,5,10,10,20,5,5,5,5,10,5,5,5,10,10,5,5,5,5,5,10,5,5,10,20,20,5,10,5,5,5,10,5,5,5,20,5,5,5,20,5,5,5,5,5,10,10,5,5,5,5,5,10,10,5,5,5,20,5,5,5,5,5,5,5,5,10,5,10,5,20,5,20,20,5,20,5,10,20,5,5,5,5,5,5,5,10,5,20,5,10,5,10,5,5,5,5,20,10,5,20,10,5,10,5,5,20,10,20,10,5,5,5,5,5,5,20,5,10,10,20,5,5,10,5,5,5,5,20,20,5,10,5,5,20,5,10]
sol= Solution()
print(sol.lemonadeChange(bills))