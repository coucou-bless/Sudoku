print("                             Welcome to Sudoku Solver!")                                    
                                                                                     
def create_grid():
    grid = []
    print("Enter the Sudoku grid row by row, use 0 for empty cells:")
    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)
    return grid

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

grid = create_grid()
if solve_sudoku(grid):
    print("Sudoku solved successfully!")
    for row in grid:
        print(" ".join(map(str, row)))
else:
    print("No solution exists.")



    