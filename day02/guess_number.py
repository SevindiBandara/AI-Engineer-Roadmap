
from random import randint, random

num = randint(1, 100)
attempts = 0
guess = int(input("Guess a number between 1 and 100: "))
while guess != num:
    attempts += 1
    if guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
print(f"Congratulations! You guessed the number in {attempts} attempts.")