class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index=0
        for i in range(len(nums1)+1):
            if i > m:
                nums1[i-1] = nums2[index]
                index+=1
        nums1.sort()
        return nums1
       
nums1=[1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n = 3
sol=Solution()
print(sol.merge(nums1,m,nums2,n))