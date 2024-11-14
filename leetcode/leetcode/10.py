"""Given an input string  and a pattern , implement regular expression matching with support for and where:sp'.''*'

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 """
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    (first_match and self.isMatch(s[1:], p)))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

                
"""import re
def matches(s, p):
    return bool(re.match(p, s))"""
        
        
        
        
s = "aa"
p = "un*"
sol = Solution()
print(sol.isMatch(s,p))
