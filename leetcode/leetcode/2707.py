class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int: #139
        stringa=""
        lista=[]
        for i in dictionary:
            stringa+=i  
        for i in s:
            if i not in stringa :
                lista.append(i)
        return len(lista)
s="leetscode"
dictionary=["leet","code","leetcode"]
sol=Solution()
print(sol.minExtraChar(s,dictionary))