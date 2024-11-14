class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1
        
        
nums= [1,7,3,6,5,6]
sol = Solution()
print(sol.pivotIndex(nums))
        
        