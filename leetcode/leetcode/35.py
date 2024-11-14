class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0 or target < nums[0]:
            return 0
        if target in nums:
            return nums.index(target)
        
        inizio = 0
        fine = len(nums) - 1
        
        while inizio <= fine:
            mid = (inizio + fine) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                inizio = mid + 1
            else:
                fine = mid - 1
        
        return inizio

                    
                
   
    
nums = [1,3,5,6]
target = 7

sol=Solution()
print(sol.searchInsert(nums,target))