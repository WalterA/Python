"""22.Date le coppie di parentesi,
scrivi una funzione per generare tutte le combinazioni di parentesi ben formate.n
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pair = "()"
        arr = []
        arr.append(pair)

        for _ in range(2,n+1):
            temp = set()

            while arr:
                val = arr.pop()
                for i in range(len(val)):
                    s = val[:i] + pair + val[i:]
                    temp.add(s)

            for t in temp:
                arr.append(t)

        return arr
            
n=3
sol = Solution()
print(sol.generateParenthesis(n))        