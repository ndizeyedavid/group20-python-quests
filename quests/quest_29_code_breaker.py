#!/usr/bin/python3

SECRET_CODE = 42


def check_guess(guess):
    """Return the result of the user's guess."""
    if guess == SECRET_CODE:
        return "Correct! You unlocked the code."
    return "Wrong code."


for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3 - Enter the secret code: "))

    print(check_guess(guess))

    if guess == SECRET_CODE:
        break

if guess != SECRET_CODE:
    print("Game Over! You have used all 3 attempts.")
