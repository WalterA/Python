class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index= 1
        index1=1
        if not s and t:
            return True
        if not t and s:
            return False
        if not t and not s:
            return True
        if len(s) == len(t):
            if s in t:
                return True
            else:
                return False
        
        
        while index < len(s)+1:
            if index1 >= len(t)+1 and index <= len(s):
                return False
            if s[index-1]==t[index1-1]:
                index+=1
                index1+=1
            else:
                index1+=1
        
        return True
       
                        
s="acb"
t = "ahbgdc"

sol=Solution()

print(sol.isSubsequence(s,t)) # Output: True
