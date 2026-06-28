secret_number = 42

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Correct! You guessed the secret number.")
