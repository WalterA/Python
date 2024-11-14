class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            if val in nums:
                nums.remove(val)
        return len(nums), nums