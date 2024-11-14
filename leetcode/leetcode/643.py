class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # inizio= 0
        # fine=k
        # massimo=sum(nums[:k])
        
        # # return massimo /k
        
        # Calcola la somma iniziale della prima finestra di lunghezza k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Scorri la lista utilizzando la tecnica della finestra scorrevole
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
        
        
        
nums = [0,0,1,1,3,3]
k=4
sol=Solution()
print(sol.findMaxAverage(nums,k))