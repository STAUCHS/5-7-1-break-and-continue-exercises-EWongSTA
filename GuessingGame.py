#-------------------------------------------------------------------------
# Name:       Guessing game
# Purpose:    guessing game with only 5 tries
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

print("** GUESS THE NUMBER **\nWelcome to guess the number game.\nYou have 5 chances to guess the number between 1-100.")
number = random.randrange(1, 101)
counter = 1
guess_remaining = 4
guess = int(input("Enter a number between 1-100: "))
print(f"Guesses remaining: {guess_remaining}")

while guess != number:
    if guess > number and counter != 5:
        print("Too high, guess again")
        guess = int(input("Enter a number between 1-100: "))
        print(f"Guesses remaining: {guess_remaining}")
        counter +=1
        guess_remaining -= 1
    elif guess < number and counter != 5:
        print("Too low, guess again")
        guess = int(input("Enter a number between 1-100: "))
        print(f"Guesses remaining: {guess_remaining}")
        counter+=1
        guess_remaining -=1
    elif guess == number and guess_remaining != 0:
        print(f"Congratulations the number was {number}")
    elif counter == 5:
        break

print(f"Sorry, you've guessed incorrectly, the number was {number}.")
