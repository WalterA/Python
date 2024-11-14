class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        result =  list(filter(lambda x: x < 0, nums))
        if len(result)  % 2 == 0:
            return 1
        else:
            return -1