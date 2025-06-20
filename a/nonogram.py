import random

def generate_nonogram(size=5):
    # Generate a random solution grid
    grid = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
    # Generate row and column clues
    def clues(line):
        c = []
        count = 0
        for cell in line:
            if cell:
                count += 1
            elif count:
                c.append(count)
                count = 0
        if count:
            c.append(count)
        return c or [0]
    row_clues = [clues(row) for row in grid]
    col_clues = [clues([grid[r][c] for r in range(size)]) for c in range(size)]
    return grid, row_clues, col_clues

def display_nonogram(row_clues, col_clues, grid=None, marks=None):
    size = len(row_clues)
    max_row = max(len(r) for r in row_clues)
    max_col = max(len(c) for c in col_clues)
    # Print column clues
    for i in range(max_col):
        print(' ' * (max_row*3), end=' ')
        for c in col_clues:
            print(f'{c[i-len(c)] if i >= len(c)-max_col else " ":>2}', end=' ')
        print()
    # Print rows
    for i, r in enumerate(row_clues):
        print(' '.join(f'{n:>2}' for n in r).rjust(max_row*3), end=' ')
        for j in range(size):
            if marks:
                print(' X' if marks[i][j] else ' .', end='')
            else:
                print(' .', end='')
        print()

def main():
    size = 5
    grid, row_clues, col_clues = generate_nonogram(size)
    marks = [[0]*size for _ in range(size)]
    print('Nonogram Puzzle:')
    display_nonogram(row_clues, col_clues)
    print('Enter moves as: row col (to toggle mark). Type "show" to reveal solution, "quit" to exit.')
    while True:
        cmd = input('> ').strip()
        if cmd == 'quit':
            break
        if cmd == 'show':
            print('Solution:')
            for row in grid:
                print(' '.join(['X' if cell else '.' for cell in row]))
            continue
        try:
            r, c = map(int, cmd.split())
            if 0 <= r < size and 0 <= c < size:
                marks[r][c] ^= 1
                display_nonogram(row_clues, col_clues, grid, marks)
            else:
                print('Out of bounds.')
        except Exception:
            print('Invalid input.')

if __name__ == '__main__':
    main()
