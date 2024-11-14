class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        # Creiamo una lista delle righe
        rows = [tuple(row) for row in grid]
        
        # Creiamo una lista delle colonne
        cols = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
        
        # Confrontiamo ogni riga con ogni colonna
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
        
        return count
