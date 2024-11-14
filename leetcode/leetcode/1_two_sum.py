
# def twoSum(nums: list[int], target: int) -> list[int] | None:
        
#         for i in range(len(nums)):
#                 for j in range(i + 1, len(nums)):      
#                         somma: int = nums[i] + nums[j]
                        
#                         if somma == target:
                                
#                                 return [i, j]
                        
#         return None
# num = [2,7,11,15]
# targe = 9
# print(twoSum(num,targe))


# def twoSum(nums: list[int], target: int) -> list[int]:
#         result = [(i,y) for i in range(len(nums)) for y in range(i+1 , len(nums)) if nums[i]+nums[y]==target]
#         if result:
#                 return result
        # for i in range(len(nums)):
        #         for j in range(i + 1, len(nums)):      
        #                 somma: int = nums[i] + nums[j]
                        
        #                 if somma == target:
                                
        #                         return [i, j]
        
        
        
        
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def ric(nums, target):
            if not nums:
                return None
            ele = nums.pop()
            for i in nums:
                if (i + ele) == target:
                    return [nums.index(i), len(nums)]
            return ric(nums, target)
        return ric(nums, target)

num = [3,3]
targe = 6
sol=Solution()
print(sol.twoSum(num,targe))
