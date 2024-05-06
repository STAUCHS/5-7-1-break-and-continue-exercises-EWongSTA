#-------------------------------------------------------------------------
# Name:       Adding up to 13
# Purpose:    adds numbers up to 13 inclusive
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------
num_start = int(input("Enter a starting number: "))
num_end = int(input("Enter an ending number: "))
sum = num_start
counter = num_start
while counter <= num_end: 
    print(f"Number: {counter} Sum: {sum}")
    if counter == 13 or counter == 31:
        break
    counter+=1
    sum+=counter
