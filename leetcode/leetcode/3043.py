class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        count = 0
        for x, y in zip(arr1, arr2):
            if x == y:
                count += len(x)
            else:
                break
        count += len(arr1[count:])
        return count
            
arr1 = [1,10,100]
arr2 = [1000]
sol=Solution()
print(sol.longestCommonPrefix(arr1,arr2))
            
        