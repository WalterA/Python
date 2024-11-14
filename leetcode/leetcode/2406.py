class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        conta=0
        for i in range(len(intervals)-1):
            temp = intervals[i][0]
            temp2 = intervals[i+1][0]
            if temp > temp2:
                conta +=1
        if len(intervals)%2==1:
            conta+=1
        if conta ==0:
            return 1
        return conta





intervals =[[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],[479815,507766],[693292,944029],[751962,821744]]
sol=Solution()
print(sol.minGroups(intervals))