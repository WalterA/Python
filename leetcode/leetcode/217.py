class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        diz={}
        for i in nums:
            if i in diz:
                diz[i]+=1
            else:
                diz[i]=1
        for i in diz.values():
            if i>1:
                return True
            
        return False
n=[2,14,18,22,22]
sol=Solution()
print(sol.containsDuplicate(n))