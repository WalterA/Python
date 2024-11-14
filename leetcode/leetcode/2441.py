class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        temp=[]
        for i in nums:
            if i <0:
                if abs(i) in nums:
                    temp.append(abs(i))
        
        if temp:
            return max(temp)
        else:
            return -1
c=[-1,2,-3,3]
sol=Solution()
print(sol.findMaxK(c))
