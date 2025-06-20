# Word Search (CLI Version)
import random

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def play_word_search():
    words = ['CAT', 'DOG', 'BEE']
    size = 6
    board = [['.' for _ in range(size)] for _ in range(size)]
    # Place words horizontally
    for idx, word in enumerate(words):
        row = idx
        col = random.randint(0, size-len(word))
        for i, ch in enumerate(word):
            board[row][col+i] = ch
    # Fill rest
    for i in range(size):
        for j in range(size):
            if board[i][j] == '.':
                board[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print('Word Search! Find these words:', ', '.join(words))
    print_board(board)
    found = set()
    while len(found) < len(words):
        guess = input('Enter found word (or q to quit): ').upper()
        if guess == 'Q':
            print('Game exited.')
            break
        if guess in words and guess not in found:
            print('Found:', guess)
            found.add(guess)
        else:
            print('Not found or already found.')
    print('All words found!')

if __name__ == '__main__':
    play_word_search()
