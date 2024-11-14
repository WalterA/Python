class Solution:
    def search(self, nums: list[int], target: int) -> int:
        sinistra, destra = 0, len(nums) - 1
        while sinistra <= destra:
            medio = (sinistra + destra) // 2
            if nums[medio] == target:
                return medio
            elif nums[medio] < target:
                sinistra = medio + 1
            else:
                destra = medio - 1
        return -1
    
nums = [-1,0,3,5,9,12]
target = 9
sol=Solution()
print(sol.search(nums,target))