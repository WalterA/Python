class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        ore = []
        for i in timePoints:
            if i == '00:00':
                ore.append(0)
            else:
                temp = int(i[:2]) * 60 + int(i[3:])
                ore.append(temp)
        ore.sort()
        min_diff = 1440  
        for i in range(1, len(ore)):
            min_diff = min(min_diff, ore[i] - ore[i - 1])
        min_diff = min(min_diff, 1440 - ore[-1] + ore[0])
        return min_diff
    
timePoints = ["00:00","23:59","00:00"]
sol=Solution()
print(sol.findMinDifference(timePoints))