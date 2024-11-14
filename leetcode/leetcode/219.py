# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # index = 0
        # while index < index +k and index +k != len(nums):
        #     if nums[index] == nums[index +k]:
        #         return True
        #     else:
        #         index += 1
        # return False
        # left= 0
        # right=k
        # if k==0:
        #     return False
        # while len(nums) != right:
        #     if nums[left] == nums[right]:
        #             if abs(right-left) <= k:
        #                 return True
        #             else:
        #                 left+=1
        #                 right+=1
                        
        #     else:
        #         left+=1
        #         right+=1
                        
        # return False

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

nums =[99,99]
k = 2
sol=Solution()
print(sol.containsNearbyDuplicate(nums,k))
#Output: true[1,2,3,1,2,3]