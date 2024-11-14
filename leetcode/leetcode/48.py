class Solution:
    def rotate(self, matrix: [list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        riga =0 
        col =0
        
        while riga != len(matrix) and col != len(matrix):
            stack= matrix.pop([riga][col])
            