class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        col= 0
        row = 0
        conta=0
        while col < len(grid):
            while row  < len(grid[0]):
                if grid[col][row] < 0:
                    conta+=1
                    row+=1
                else:
                    row+=1
            row = 0
            col+=1
        return  conta
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
sol=Solution()
print(sol.countNegatives(grid))