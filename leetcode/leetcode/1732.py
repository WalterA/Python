class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        highest_altitude = 0
        
        for g in gain:
            current_altitude += g
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude
        
        return highest_altitude
gain = [-5,1,5,0,-7]
sol=Solution()
print(sol.largestAltitude(gain))