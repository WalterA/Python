class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        conta = 0
        
        while left < right:
            if nums[left] + nums[right] == k:
                conta += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
                
        return conta
num = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
ok=2
sol=Solution()
print(sol.maxOperations(num,ok))