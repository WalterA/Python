class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        #soluzione trovata dal sito
        
        totalSum = sum(nums)
        rem = totalSum % p

        if rem == 0:
            return 0

        prefixMod = {0: -1}
        prefixSum = 0
        minLength = len(nums)

        for i, num in enumerate(nums):
            prefixSum += num
            currentMod = prefixSum % p
            targetMod = (currentMod - rem + p) % p

            if targetMod in prefixMod:
                minLength = min(minLength, i - prefixMod[targetMod])

            prefixMod[currentMod] = i

        return minLength if minLength < len(nums) else -1


n=[6,3,5,2]
p=9
sol=Solution()
print(sol.minSubarray(n,p))
        
                
        
                