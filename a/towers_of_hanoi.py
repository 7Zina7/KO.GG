def print_hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
    else:
        print_hanoi(n-1, source, auxiliary, target, moves)
        moves.append((source, target))
        print_hanoi(n-1, auxiliary, target, source, moves)

def main():
    print('Towers of Hanoi (CLI)')
    n = int(input('Enter number of disks (3-6 recommended): '))
    moves = []
    print_hanoi(n, 'A', 'C', 'B', moves)
    print(f'Solution in {len(moves)} moves:')
    for i, (src, tgt) in enumerate(moves, 1):
        print(f'Move {i}: {src} -> {tgt}')

if __name__ == '__main__':
    main()
