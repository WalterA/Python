class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        copy= score.copy()
        copy.sort(reverse=True)
        index=0
        lista=[]
        while index!=len(copy):
                if score[index] == copy[0]:
                    lista.append("Gold Medal")
                    index+=1
                elif score[index] == copy[1]:
                        lista.append("Silver Medal")
                        index+=1
                elif score[index] == copy[2]:
                    lista.append("Bronze Medal")
                    index+=1
                else:
                    ind= copy.index(score[index])
                    lista.append(str(ind+1)) 
                    index+=1      
        return lista
        
        
score = [10,3,8,9,4]
sol=Solution()
print(sol.findRelativeRanks(score))