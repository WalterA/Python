class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        copy=heights.copy()
        copy.sort()
        conta=0
        for i in range(len(heights)):
            if heights[i] != copy[i]:
                conta+=1
        return conta
        """
        #return sum(h1!=h2 for h1, h2 in zip(heights, sorted(heights)))
        # sorted_heights = sorted(heights)
        # count = 0

        # for h1, h2 in zip(heights, sorted_heights):
        #     if h1 != h2:
        #         count += 1

        # return count
        
heights = [1,1,4,2,1,3]
sol=Solution()
print(sol.heightChecker(heights))