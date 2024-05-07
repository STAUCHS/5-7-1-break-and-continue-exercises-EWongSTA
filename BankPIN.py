#-------------------------------------------------------------------------
# Name:       Bank Pin
# Purpose:    asks user for their bank pin (with while loops)
# Author:     Wong. E
# Created:    06/05/2024
#-------------------------------------------------------------------------


print("WELCOME TO STA BANK!")

bank_pin = 3145
enter_pin = int(input("Enter your bank pin: "))

while enter_pin != bank_pin:
    if enter_pin == bank_pin:
        break
    print("Incorrect PIN. Please try again")
    

print("PIN accepted. You may now access your account")
