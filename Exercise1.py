import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess?'))

        if user_guess == answer:
            print(f'Right! The answer is (user_guess)')
            break

        if user_guess < answer:
            print(f'You guess of (user_guess) is too low!')
        else:
            print(f'Your guess of (user_guess) is to high!')
guessing_game()