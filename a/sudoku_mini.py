# Sudoku Mini (4x4) - CLI Version
import random

def print_board(board):
    for row in board:
        print(' '.join(str(x) if x != 0 else '.' for x in row))
    print()

def is_valid(board, r, c, n):
    for i in range(4):
        if board[r][i] == n or board[i][c] == n:
            return False
    br, bc = 2*(r//2), 2*(c//2)
    for i in range(2):
        for j in range(2):
            if board[br+i][bc+j] == n:
                return False
    return True

def solve(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                for n in range(1,5):
                    if is_valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def play_sudoku():
    # Pre-filled easy puzzle
    board = [
        [1, 0, 0, 4],
        [0, 0, 1, 0],
        [0, 3, 0, 0],
        [2, 0, 0, 3]
    ]
    print('Sudoku Mini (4x4)! Fill the grid so each row, column, and box has 1-4.')
    while True:
        print_board(board)
        if all(all(cell != 0 for cell in row) for row in board):
            print('Puzzle complete!')
            break
        try:
            move = input('Enter row,col,num (e.g. 1,2,3) or q to quit: ')
            if move.lower() == 'q':
                print('Game exited.')
                break
            r, c, n = map(int, move.split(','))
            if board[r][c] == 0 and is_valid(board, r, c, n):
                board[r][c] = n
            else:
                print('Invalid move.')
        except Exception:
            print('Invalid input.')

if __name__ == '__main__':
    play_sudoku()
