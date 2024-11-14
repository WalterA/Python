class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = bin(start)[2:]
        y = bin(goal)[2:]
        
        # Calcola la differenza di lunghezza e aggiungi zeri iniziali alla stringa più corta
        if len(x) > len(y):
            y = y.zfill(len(x))
        else:
            x = x.zfill(len(y))
        
        conta = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                conta += 1
                
        return conta

start = 10
goal = 82
sol=Solution()
print(sol.minBitFlips(start,goal))
