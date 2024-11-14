class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if blue % 2 ==0:
            blue-=1
        if blue-=1 == 0:
            
            