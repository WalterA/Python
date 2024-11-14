class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # diz={}
        # for i in stones:
        #     if i in jewels:
        #         if i in diz:
        #             diz[i]+= 1
        #         else:
        #             diz[i]=1
        # return sum(diz.values())
        index= 0
        count=0
        while index < len(stones):
            if stones[index] in jewels:
                count += 1
            index += 1
        return count
jewels = "aA"
stones = "aAAbbbb"
sol=Solution()
print(sol.numJewelsInStones(jewels,stones))