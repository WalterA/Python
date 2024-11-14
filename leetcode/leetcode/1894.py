class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        
        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed

                
        
c=[22,86,96,35,62,69,56,33,95,10,38,53,33,90,29,68,85,58,11,49,81,18,32,96,40,75,49,26,60,71,15,94,31,99,12,81,10,19,7,73,35,56,100,15,37,89,58,17,55,62,4,30,68,68,89,62,39,35,16,18,63,73,100,22,46,58,80,77,23,5,52,96,98,21,33,86,81,71,69,72,71,58,17,85,70,22,84,94,75,51,60,81,12,22,13,33,53,58]
k=134221332
sol=Solution()
print(sol.chalkReplacer(c,k))