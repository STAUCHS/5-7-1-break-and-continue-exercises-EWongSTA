#-------------------------------------------------------------------------
# Name:       Simple Loop
# Purpose:    Simple loop that counts from 1-10 but skips 7
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------

sum = 0
while True:
    sum +=1
    if sum == 7:
        continue
    if sum > 10:
        break
    print(sum)
