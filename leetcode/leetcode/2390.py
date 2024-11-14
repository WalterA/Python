class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    """class Solution:
    def removeStars(self, s: str) -> str:
        x= list(s)
        i=0
        
        while i!=len(x):
            if x[i] == "*":
                x.pop(i)
                i-=1
                x.pop(i)
                
            else:
                i+=1
        return "".join(x)"""
s = "leet**cod*e"
sol=Solution()
print(sol.removeStars(s))
 