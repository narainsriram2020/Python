# Python Guess the Number
#
# Description: Game for user to guess a random number
#
# Author: Narain Sriram

import random

num_of_guess = 0
tries = 0
play = print("Hello Welcome to Guess the Number!")
x = int(input("What would you like the range of the first number to be?\n"))
y = int(input("What would you like the range of the second number to be?\n"))
print("Your guesses should be in between", x, "and including", y)
scrt_num = random.randrange(x, y)
z = y + 1  # Variable for the give up number
print("If you want to give up then enter ", z)

while True:
    guess = int(input("What is your guess? "))
    if guess == z: # If they enter the give up number then this statement is run
        print("Please don't give up, persevere and become stronger")
        break
    
    if guess < x or guess > y: # If the user enter and invalid number the following number will be displayed
        print("Your guess is not in the proper intervals")
        print("Please enter a proper value")

    if guess > scrt_num: # For the guess being higher than the number
        print("Your guess is too high. You have to guess lower")
        num_of_guess += 1

    if guess < scrt_num: # For the guess being lower than the number
        print("Your guess is too low. You have to guess higher")
        num_of_guess += 1
        
    if guess == scrt_num: # If the number is guessed
        print("Congratulations! You guessed the secret number!")
        print("It took you", num_of_guess, "guesses to find the secret number")
        print("The secret number was: ", scrt_num)
        num_of_guess += 1
        break
