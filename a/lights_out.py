# Lights Out Game (Python, CLI version)
import random

def create_board(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(' '.join(['O' if cell else '.' for cell in row]))
    print()

def toggle(board, x, y):
    size = len(board)
    for dx, dy in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < size and 0 <= ny < size:
            board[nx][ny] ^= 1

def is_win(board):
    return all(cell == 0 for row in board for cell in row)

def play_lights_out(size=5):
    board = create_board(size)
    print('Welcome to Lights Out!')
    while True:
        print_board(board)
        if is_win(board):
            print('You win!')
            break
        try:
            move = input('Enter row,col (e.g. 2,3) or q to quit: ')
            if move.lower() == 'q':
                print('Game exited.')
                break
            x, y = map(int, move.split(','))
            toggle(board, x, y)
        except Exception:
            print('Invalid input. Try again.')

if __name__ == '__main__':
    play_lights_out()
