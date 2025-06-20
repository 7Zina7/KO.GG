import random

def generate_pattern(length=6, colors=None):
    if colors is None:
        colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    return [random.choice(colors) for _ in range(length)]

def main():
    print('Color Pattern Memory Game')
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    pattern = generate_pattern()
    print('Memorize this pattern:')
    print(' '.join(pattern))
    input('Press Enter when ready to continue...')
    print('\n' * 50)  # Clear screen
    guess = input('Enter the pattern (space-separated, e.g. R G B Y O P): ').strip().split()
    if guess == pattern:
        print('Correct!')
    else:
        print('Incorrect. The pattern was:', ' '.join(pattern))

if __name__ == '__main__':
    main()
