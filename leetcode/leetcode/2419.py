class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = max(nums)  # Trova il valore massimo nell'array
        max_len = 0
        current_len = 0
        
        for num in nums:
            if num == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        
        return max_len
    
nums=[100,5,5]
sol=Solution()
print(sol.longestSubarray(nums))