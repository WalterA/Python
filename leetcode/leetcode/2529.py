class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg=0
        pos=0
        for i in nums:
            if i != 0:
                if i > 0:
                    pos+=1
                else:
                    neg+=1
        return max(pos, neg)
nums = [-2,-1,-1,1,2,3]
sol=Solution()
print(sol.maximumCount(nums))
            