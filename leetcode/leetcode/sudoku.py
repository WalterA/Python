def valid_sudoku(board):
    def is_valid_unit(unit):
        # Filtra i numeri e ignora i punti
        unit = [i for i in unit if i != '.']
        # Controlla se ci sono duplicati
        return len(unit) == len(set(unit))
    
    def is_valid_row(board):
        # Controlla ogni riga
        for row in board:
            if not is_valid_unit(row):
                return False
        return True

    def is_valid_col(board):
        # Controlla ogni colonna
        for col in range(9):
            if not is_valid_unit([board[row][col] for row in range(9)]):
                return False
        return True

    def is_valid_square(board):
        # Controlla ogni sottoriquadro 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(square):
                    return False
        return True
    
    # Verifica le tre condizioni: righe, colonne e quadrati
    return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
    
    
    
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
valid_sudoku(board)