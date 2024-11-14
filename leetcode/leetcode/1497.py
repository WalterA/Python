class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        #unica soluzione dal sito
        mp = [0] * k

        # Count occurrences of each remainder
        for x in arr:
            rem = (x % k + k) % k  # Ensure non-negative remainder
            mp[rem] += 1

        # Check pairing conditions
        for i in range(k):
            if i == 0:
                # Remainder 0 must appear in even count
                if mp[i] % 2 != 0:
                    return False
            else:
                # Remainders must match
                if mp[i] != mp[k - i]:
                    return False

        return True
arr = [1,2,3,4,5,6]
k = 10
sol=Solution()
print(sol.canArrange(arr, k))
                        
                
            