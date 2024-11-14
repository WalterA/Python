class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        Find all valid combinations of numbers that sum up to such that the following conditions are true:kn
        Only numbers through are used.19
        Each number is used at most once.
        Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
        """
        lista = [1,2,3,4,5,6,7,8,9]
        res = []
        self.backtrack(res, [], k, n, lista)
        return res
    
    def backtrack(self, res, path, k, n, lista):
        if len(path) == k and sum(path) == n:
            res.append(path.copy())
            return
        
        if len(path) >= k or sum(path) > n:
            return
        
        for i in range(len(lista)):
            path.append(lista[i])
            self.backtrack(res, path, k, n, lista[i+1:])
            path.pop()
        
k = 3
n = 7
sol=Solution()
print(sol.combinationSum3(k,n))