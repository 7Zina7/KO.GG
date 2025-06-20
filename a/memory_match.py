# Memory Match (CLI Version)
import random

def create_board(size=4):
    pairs = list(range(1, size*size//2+1)) * 2
    random.shuffle(pairs)
    board = [pairs[i*size:(i+1)*size] for i in range(size)]
    revealed = [[False]*size for _ in range(size)]
    return board, revealed

def print_board(board, revealed):
    for i, row in enumerate(board):
        print(' '.join(str(val) if revealed[i][j] else '*' for j, val in enumerate(row)))
    print()

def play_memory_match(size=4):
    board, revealed = create_board(size)
    print('Memory Match! Find all pairs.')
    moves = 0
    while not all(all(row) for row in revealed):
        print_board(board, revealed)
        try:
            a = input('First card (row,col): ')
            if a == 'q': break
            b = input('Second card (row,col): ')
            if b == 'q': break
            r1, c1 = map(int, a.split(','))
            r2, c2 = map(int, b.split(','))
            if revealed[r1][c1] or revealed[r2][c2] or (r1==r2 and c1==c2):
                print('Invalid pick.')
                continue
            revealed[r1][c1] = revealed[r2][c2] = True
            print_board(board, revealed)
            if board[r1][c1] != board[r2][c2]:
                print('No match!')
                revealed[r1][c1] = revealed[r2][c2] = False
            else:
                print('Match!')
            moves += 1
        except Exception:
            print('Invalid input.')
    print('Game over! Moves:', moves)

if __name__ == '__main__':
    play_memory_match()
