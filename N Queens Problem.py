def is_safe(board, row, col, n):
    # Check column upwards
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        # Found a valid solution, copy it
        solution = ["".join(r) for r in board]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = '.'  # Backtrack

def nqueens_solver(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions

# Example usage:
n = int(input("Enter number of queens (N): "))
solutions = nqueens_solver(n)
print(f"Number of solutions: {len(solutions)}\n")

for idx, sol in enumerate(solutions, 1):
    print(f"Solution #{idx}:")
    for row in sol:
        print(row)
    print()