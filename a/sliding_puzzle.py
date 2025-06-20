# Sliding Puzzle (8-puzzle) - CLI Version
import random

def create_board(size=3):
    nums = list(range(size*size))
    random.shuffle(nums)
    return [nums[i*size:(i+1)*size] for i in range(size)]

def print_board(board):
    for row in board:
        print(' '.join(str(x) if x != 0 else '.' for x in row))
    print()

def find_zero(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def move(board, direction):
    size = len(board)
    x, y = find_zero(board)
    dx, dy = {'w':(-1,0),'s':(1,0),'a':(0,-1),'d':(0,1)}.get(direction, (0,0))
    nx, ny = x+dx, y+dy
    if 0 <= nx < size and 0 <= ny < size:
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        return True
    return False

def is_win(board):
    size = len(board)
    nums = [board[i][j] for i in range(size) for j in range(size)]
    return nums == list(range(1, size*size)) + [0]

def play_sliding_puzzle(size=3):
    board = create_board(size)
    print('Sliding Puzzle! Use w/a/s/d to move the empty space.')
    while True:
        print_board(board)
        if is_win(board):
            print('You win!')
            break
        move_input = input('Move (w/a/s/d) or q to quit: ')
        if move_input == 'q':
            print('Game exited.')
            break
        if not move(board, move_input):
            print('Invalid move.')

if __name__ == '__main__':
    play_sliding_puzzle()
