"""Given an integer array and an integer , return the largest element in the array.numskkth

Note that it is the largest element in the sorted order, not the distinct element.kthkth

Can you solve it without sorting?"""
class Solution:
    def ok(self,lim,conta,nums):
        while lim !=conta:
            valore_minimo = min(nums)
            nums.remove(valore_minimo)
            conta+=1
        return valore_minimo
    
    
    def findKthLargest(self, nums: list[int], k: int) -> int:
        conta=0
        lim=len(nums)-k+1
        x = self.ok(lim,conta,nums)
        return x
    
    


# import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = nums[:k] # Initialize a min-heap with the first k elements from nums
        heapq.heapify(min_heap) # Transform the list into a min-heap
        for num in nums[k:]:
            if num > min_heap[0]: # If the current element is larger than the smallest element in the heap
                heapq.heappushpop(min_heap, num) # Replace the smallest element (root of the min-heap) with the current element
        return min_heap[0]

"""
        lim=len(nums)-k+1
        while lim != 0:
            max_num = max(nums)
            nums.remove(max_num)
            lim -= 1
        return max_num
"""
# Example 1:
nums = [3,2,1,5,6,4]
k = 2
sol=Solution()
print(sol.findKthLargest(nums,k))