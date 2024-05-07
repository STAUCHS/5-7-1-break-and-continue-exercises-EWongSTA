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
    if user != enter_user and password != enter_pass:
        print("Username and password incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user == enter_user and password != enter_pass:
        print("Password incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user != enter_user and password == enter_pass:
        print("Username incorrect")
        enter_user = input("Enter your username: ")
        enter_pass = input("Enter your password: ")
    elif user == enter_user and password == enter_pass:
        break

print("Welcome!")