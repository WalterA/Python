class Solution:
    def reverseWords(self, s: str) -> str:
        
        lista = s.split()
        index=len(lista)
        stringa = []
        
        for i in range(len(lista) - 1, -1, -1):
            stringa.append(lista[i])
            stringa.append(" ")
        stringa.pop()
        return "".join(stringa)
    
    """s = s.split()[::-1]
        print(s)
        s = " ".join(s)
        return s"""
    
s = "the sky is blue"
sol= Solution()
print(sol.reverseWords(s))