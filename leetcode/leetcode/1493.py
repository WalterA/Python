class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0
        k=1
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length-1

n=[0,1,1,1,0,1,1,0,1]
sol = Solution()
print(sol.longestSubarray(n))
