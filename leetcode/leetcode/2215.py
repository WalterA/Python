class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        puliti1 = list(set(nums1))
        puliti2 = list(set(nums2))
        temp=[]
        temp2=[]
        for i in puliti1:
            if i not in puliti2:
                temp.append(i)
        for i in puliti2:
            if i not in puliti1:
                temp2.append(i)
        result=[]
        result.append(temp)
        result.append(temp2)
        return result
                
                
        
        
nums1 = [1,2,3,3] #123
                  #12  #[[3],[]]
nums2 = [1,1,2,2]
sol=Solution()
print(sol.findDifference(nums1,nums2))