#-------------------------------------------------------------------------
# Name:       Usernamepassword
# Purpose:    Enter your username and password to enter
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

user = "StAugustineCHS"
password = "Coding123"

enter_user = input("Enter your username: ")
enter_pass = input("Enter your password: ")

while True:
    if user != "StAugustineCHS" and password != "Coding123":
        print("Username and password incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user == "StAugustineCHS" and password != "Coding123":
        print("Password incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user != "StAugustineCHS" and password == "Coding123":
        print("Username incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user == "StAugustineCHS" and password == "Coding123":
        break

print("Welcome!")