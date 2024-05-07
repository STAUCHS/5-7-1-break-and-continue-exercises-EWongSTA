#-------------------------------------------------------------------------
# Name:       adding 5-20
# Purpose:    adds numbres from 5 - 20 inclusive
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------
x = 4
sum = 0
while x < 21:
    x += 1
    if x%3 == 0:
        continue
    else:
        sum += x
        print(sum)