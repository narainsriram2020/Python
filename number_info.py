# Python Number Info
#
# File that prints out a set of information for a user-input number
#
# Author: Narain Sriram

m = 0
user_num = int(input("Please enter a positive number: "))
# Question asking user to enter a number
if user_num < 1:
    print("That is not a positive number!") # If not positive then this is played
else:
    print(user_num) # The number entered by the user is printed

    def odd_or_even(num): # This is my def function where i have created an if statement to show whether a number is odd or even
        if num % 2 == 1:
            num_type = "Odd"
        else:
            num_type = "Even"
        return num_type

# I then "plug in" user_num into the def and get my final answer. I then print that answer
    print(odd_or_even(user_num))

    # Created a method to check if the number is prime or not
    def prime_check(num):
        good = True # Flag Variable to know whether the result is good or not
        for i in range(2, int(num/2) + 1):
            if num % i == 0: # If it is divisible by any number within the range of i, then it is considered Not Prime
                good = False
                m = i
        if good:
            print("Prime")
        else:
            print("Not Prime")
            print("Greatest Factor:", m)
    prime_check(user_num) # Print the final statement

        
   
