class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x=ransomNote.lower()
        y=magazine.lower()
        for i in x:
            if i not in y:
                return False
            else:
                y=y.replace(i, '', 1)
        return True
s="aa"
d="ab"
sol=Solution()
print(sol.canConstruct(s,d))