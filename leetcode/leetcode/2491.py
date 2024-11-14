class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        temp3=[]
        while len(skill) !=0:
            temp1=skill.pop()
            temp2=skill.pop(0)
            temp3.append([temp1,temp2])
        fine=len(temp3)-1
        for i in range(len(temp3)):
            if sum(temp3[i])== sum(temp3[fine]):
                if i == fine:
                    break
            else:
                return -1
        lista=[]
        for i in range(len(temp3)):
            temp= temp3[i][0]*temp3[i][1]
            lista.append(temp)
        return sum(lista)
                
            
        
skill = [3,2,5,1,3,4]         
sol=Solution()
print(sol.dividePlayers(skill))