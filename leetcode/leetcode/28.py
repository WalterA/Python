class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

s="hello"
a="ll"
sol=Solution()
print(sol.strStr(s,a))