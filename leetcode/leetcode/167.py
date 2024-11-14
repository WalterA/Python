class Solution:
    def twoSum(self,  numbers: list[int], target: int) -> list[int]:
        copy=numbers.copy()
        copy=copy[::-1]
        for i in range(len(numbers)-1):
            if numbers[i] + copy[i] ==target:
                return [i,] 
        
        
        
        
        
        
        
        
s=[3,3,2]
f=6
sol=Solution()
print(sol.twoSum(s,f))
