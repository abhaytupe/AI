# Constraint Satisfaction Problem using Backtracking
## N-Queens Problem
## Aim

# Implement a solution for Constraint Satisfaction Problem using Backtracking for the N-Queens problem.
# ## Theory

# The N-Queens problem is a classic Constraint Satisfaction Problem.

# The objective is to place N queens on an N×N chessboard such that:
# - No two queens attack each other
# - No queens share the same row
# - No queens share the same column
# - No queens share the same diagonal

# Backtracking is used to find the valid arrangement.
# N-Queens Problem using Backtracking

N = 4

board = [[0 for x in range(N)] for y in range(N)]

def is_safe(board, row, col):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col

    while j >= 0 and i < N:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True

def solve_nq(board, col):

    # If all queens are placed
    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):

            board[i][col] = 1

            if solve_nq(board, col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False

def print_solution(board):

    print("Solution:")

    for i in range(N):

        for j in range(N):
            print(board[i][j], end=" ")

        print()

if solve_nq(board, 0):

    print_solution(board)

else:
    print("No solution exists")
## Conclusion

# The N-Queens problem was solved successfully using Backtracking.
# The algorithm places queens safely by checking constraints recursively.
