def is_valid_move(grid, row, col, number):
    # Check if the number is already in the given row
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    # Check if the number is already in the given column
    for x in range(9):
        if grid[x][col] == number:
            return False
        
    # Determine the top-left corner of the 3x3 subgrid that contains the cell (row, col)
    corner_row = row - row % 3
    corner_col = col - col % 3

    # Check if the number is already in the 3x3 subgrid
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    
    # If the number is not found in the row, column, or 3x3 subgrid, the move is valid
    return True

def solve(grid, row, col):
    # If the column index exceeds 8, move to the next row and reset column index to 0
    if col == 9:
        if row == 8:
            # If we're at the last row and column, the grid is successfully solved
            return True
        row += 1
        col = 0
    
    # If the cell already contains a number, move to the next cell
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    # Try placing numbers 1 through 9 in the current empty cell
    for num in range(1, 10):
        # Check if placing the number is valid
        if is_valid_move(grid, row, col, num):
            # Place the number on the grid
            grid[row][col] = num

            # Recursively attempt to solve the grid with the new number in place
            if solve(grid, row, col + 1):
                return True
            
            # If the number does not lead to a solution, reset the cell (backtrack)
        grid[row][col] = 0

    # If no number between 1 and 9 can be placed in this cell, return False (trigger backtracking)
    return False

# Initial Sudoku grid with some cells filled and others set to 0 (empty)
grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# Attempt to solve the Sudoku puzzle
if solve(grid, 0, 0):
    # If a solution is found, print the solved grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    # If no solution exists, print a message
    print("No solution for this sudoku")
