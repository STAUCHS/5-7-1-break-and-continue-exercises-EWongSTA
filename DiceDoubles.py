#-------------------------------------------------------------------------
# Name:       Dice Doubles
# Purpose:    Rolls until you get doubles
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

while True:
 roll_1 = random.randrange(1, 7)
 roll_2 = random.randrange(1, 7)
 print(f"Roll #1: {roll_1}")
 print(f"Roll #2: {roll_2}")
 print(f"The total is {roll_1 + roll_2}!")
 if roll_1 == roll_2:
  break
 

