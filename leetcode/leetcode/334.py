class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
    
nums = [20,100,10,12,5,13]
sol=Solution()
print(sol.increasingTriplet(nums))