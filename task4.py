def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
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


# 🔹 USER INPUT
board = []
print("Enter the Sudoku row by row")
print("Use 0 for empty cells")
print("Example: 5 3 0 0 7 0 0 0 0\n")

for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    board.append(row)

print("\nOriginal Sudoku:\n")
print_sudoku(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:\n")
    print_sudoku(board)
else:
    print("No solution exists")
