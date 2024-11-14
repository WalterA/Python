class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        nums.sort()
        m=nums[-1]
        for i in range(len(nums)-1):
            m=min(m, abs(nums[i]-nums[i+1]))
        return m
    
sos = Solution()
print(sos.findValueOfPartition([100,1,10]))

"""Input:v
Output: 1
Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.
Esempio 2:

Input: nums = [100,1,10]
Output: 9
Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions."""

#|max(nums1) - min(nums2)|