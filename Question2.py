#-------------------------------------------------------------------------
# Name:       
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
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