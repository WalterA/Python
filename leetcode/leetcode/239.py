from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        #TENTATIVO N1 Memory Limit Exceeded
        massimo = []
        index=0
        def ric(nums, k,massimo,index ):
            gruppo = nums[index:k]
            massimo.append(max(gruppo))
            index+=1
            k+=1
            if k > len(nums):
                return massimo
            else:
                return ric(nums,k,massimo,index)
        return ric(nums, k,massimo,index )
        
        #TENTATIVO N2 Memory Limit Exceeded
        massimo = []
        for i in range(len(nums)):
            massimo.append(max(nums[i:k]))
            if k == len(nums):
                return massimo
            else:
                k+=1
        return massimo
        
        #TENTATIVO N3 Memory Limit Exceeded
        gruppo = []
        maxy = []

        for i in range(len(nums), k):
            maxy.append(max(nums[i:k]))
            k+1
        return maxy
        
        #TENTATIVO N4 Memory Limit Exceeded    
        maxy=[]
        fine= len(nums)-k
        
        for i in range(len(nums)):
            maxy.append(max(nums[i:k]))
            k+=1
            if i == fine:
                return maxy
        
        #SOLUZIONE DEQU     
        from collections import deque
        from typing import List

        
        if not nums:
            return []
        
        deq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove elements smaller than the current element
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)
            
            # Append the maximum element of the current window to the result
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
        """
        if not nums:
            return []
        deq = deque(nums)
        result=[]
        group=[]
        
        while deq:
            group.append(deq.popleft())
            if len(group) == k:
                result.append(max(group))
                for i in group[1:]:
                    deq.appendleft(i)
                group.clear()
        return result
        

# Esempio di utilizzo
nums=[1,3,-1,-3,5,3,6,7]
k=3
sol=Solution()
print(sol.maxSlidingWindow(nums,k))
            
