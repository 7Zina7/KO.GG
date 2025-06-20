import random
import time

def generate_sequence(length=5, colors=None):
    if colors is None:
        colors = ['R', 'G', 'B', 'Y']
    return [random.choice(colors) for _ in range(length)]

def main():
    print('Simon Says (CLI)')
    colors = ['R', 'G', 'B', 'Y']
    score = 0
    while True:
        seq = generate_sequence(score+1, colors)
        print('Watch the sequence:')
        for color in seq:
            print(color, end=' ', flush=True)
            time.sleep(0.7)
        print('\n' * 30)
        guess = input(f'Enter the sequence (space-separated, {len(seq)} colors): ').strip().split()
        if guess == seq:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. The sequence was:', ' '.join(seq))
            print(f'Game over! Your score: {score}')
            break

if __name__ == '__main__':
    main()
