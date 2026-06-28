# Quest 18: The Loop of Riddles
# Concept: while loop with user-input condition - guessing game

import random

print("=== Quest 18: The Loop of Riddles ===")
print("I have chosen a secret number between 1 and 20.")
print("Can you guess it?\n")

secret_number = random.randint(1, 20)
guess = None
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"\nCorrect! The secret number was {secret_number}.")
            print(f"You cracked the riddle in {attempts} attempt(s)!")
    except ValueError:
        print("Please enter a valid whole number.\n")
