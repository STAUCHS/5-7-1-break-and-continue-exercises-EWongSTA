#-------------------------------------------------------------------------
# Name:       Ask For Word
# Purpose:    ASk user for a word
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------

word = input("Enter a word: ")

while True:
    if word == "stop":
        break
    print(f"Your word: {word}")

print("Goodbye!")