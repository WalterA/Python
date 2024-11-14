class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        diz={}
        for i in nums:
            if i in diz:
                diz[i]+=1
            else:
                diz[i]=1
        temp=0
        temp1=0
        for k,v in diz.items():
            if temp < v:
                temp=v
                temp1=k
        return temp1
nums = [3,2,3]
sol=Solution()
print(sol.majorityElement(nums))