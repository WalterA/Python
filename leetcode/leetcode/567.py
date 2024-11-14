class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #gpt
        from collections import Counter
        s1_count = Counter(s1)
        window_count = Counter()
        for i, char in enumerate(s2):
            window_count[char] += 1
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1
            if window_count == s1_count:
                return True
        return False

s1="ab"
s2="eidboaoo"
sol=Solution()
print(sol.checkInclusion(s1,s2))