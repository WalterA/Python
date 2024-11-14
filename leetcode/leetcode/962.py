class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        massimo = 0
        lista= list(enumerate(nums))
        ultimo =lista.pop()
        while lista:
            for i in lista:
                if i[0] < ultimo[0] and i[1] <= ultimo[1]:
                    temp= ultimo[0] -i[0]
                    if massimo < temp:
                        massimo = temp
            ultimo =lista.pop()
                
                    
        return massimo
n=[6,0,8,2,1,5]
sol=Solution()
print(sol.maxWidthRamp(n))

"""class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        massimo=0
        n=len(nums)
        for i,v in enumerate(nums):
            for j in range(n-1, -1, -1):
                if i < j and v<=nums[j]:
                    temp=j-i
                    if massimo < temp:
                        massimo = temp
        return massimo"""