class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        # for i in range(len(nums) - k + 1):
        #     subrange = nums[i:i + k]
        #     if len(set(subrange))>= k:
        #         nums[i]=sum(list(set(subrange)))
        #     else:
        #         if len(nums)==k:
        #             return 0
        #         else:
        #             return 0
        # return max(nums)
        """
        nums= list(set(nums))
        n=len(nums)
        maxy=sum(nums[:k])
        window=maxy
        if n<k:
            return 0
        for i in range(n-k):
            window= window- nums[i] + nums[i+k]
            maxy=max(maxy,window)
        return maxy
        """
                
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        num_count = {}
        
        for i in range(len(nums)):
            # Aggiungi l'elemento corrente alla finestra
            current_sum += nums[i]
            num_count[nums[i]] = num_count.get(nums[i], 0) + 1
            
            # Rimuovi l'elemento che esce dalla finestra
            if i >= k:
                current_sum -= nums[i - k]
                num_count[nums[i - k]] -= 1
                if num_count[nums[i - k]] == 0:
                    del num_count[nums[i - k]]
            
            # Controlla se la finestra ha esattamente k elementi distinti
            if i >= k - 1 and len(num_count) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

# Esempio di utilizzo
sol = Solution()
nums = [1, 2, 3, 4, 5, 6]
k = 3
print(sol.maximumSubarraySum(nums, k))  # Output: 15 (somma di [4, 5, 6])


    
            
nums = [1,1,1,1,1,1]
k = 2
sol=Solution()
print(sol.maximumSubarraySum(nums,k))
          
                