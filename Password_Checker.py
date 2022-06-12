# Python Password Checker
#
# Description: A password checker that checks for the security of the password
#
# Author: Narain Sriram

print("Hello! Welcome to the Python Password Checker. You can    enter you're password and I will check it to tell you     about its security.")

while True:
    password = input("Please enter your password:\n") # Input asking for the user to enter their password

    if len(password) < 8: #Should be 8 characters
        print("Your Password is not long enough")

    if password.find (" ") != -1: #Shouldn't contain spaces
        print("You have a space for the first character. You need a      letter for the first character.")

    first_letter = password[0] #Should begin with a letter 
    lower1 = first_letter.lower
    upper1 = first_letter.upper
    if lower1 == upper1:
        print("The password should begin with a letter")

    upper = password.upper() 
    #Should contain at least one uppercase and lowercase letter
    lower = password.lower()
    if not password == upper and password == lower:
        print("The password should contain at leat one uppercase and one lowercase letter")
    
    num_value = 0
    while num_value <= 9:
        if password.find(str(num_value)) != -1:
            break
        num_value += 1
    if not num_value < 9:
        print("You need numbers in your password")

#Contain a special character
    if password.find("!") == -1 and password.find("@") == -1 and password.find("$") == -1 and password.find("&") == -1 and password.find("?")== -1:
        print("You need to have one of the following characters in your  password: !, @, $, &, ?")
    else:
        print("\nThe password entered is secure")
    break


           
