class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        maxprof = 0
        temp = 0
        for i in range(1,len(prices)):
            if min > prices[i]:
                min = prices[i]
            temp = prices[i] - min
            if maxprof < temp:
                maxprof = temp
        return maxprof          

prices = [7,1,5,3,6,4]
sol = Solution()

print(sol.maxProfit(prices))