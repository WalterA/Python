class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        conta=0
        while index != len(nums)- conta:
            if nums[index] == 0:
                nums.remove(0)
                nums.append(0)
                conta +=1
            else:
                index +=1
        return nums
        
nums=[0,1,0,3,12]
sol= Solution()
print(sol.moveZeroes(nums))