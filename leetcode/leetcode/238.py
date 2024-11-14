class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length
        
        # Calculate left products
        left_product = 1
        for i in range(length):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
nums = [-1,-1,0,-1,-1]
sol=Solution()
print(sol.productExceptSelf(nums))