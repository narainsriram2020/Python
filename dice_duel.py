# Python Dice Duel
#
# Description: This program is a simple dice game between the computer and the user
#
# Author: Narain Sriram

import random
print("Welcome to Dice Duel! Here we go!")
u = int(input("Please enter your roll: "))
# The code below will help distinguish the cheating aspect to the game:
if u > 6:
    print("You cheated! I win!")
else:
    c = random.randrange(1,7,1)
    print("My roll was:", c)
    pu = 0
    pc = 0
# First part meant to measure greater than or less than
    if c == u:
        pc = 0
        pu = 0
    elif c > u:
        pc = pc + 1
    elif c < u:
        pu = pu + 1

# Second part meant to measure the sum of the two
# Use modular Division intead of randrange
    if c % u == 1:
        pc = pc + 1
    else:
        pu = pu + 1

# Print final statements regarding who won the game
    if pc > pu:
        print("I win! The score was", pu, "to", pc)
    if pu > pc:
        print("You win! The score was", pu, "to", pc)
    if pc == pu:
        print("Neither of us win! The score was", pu, "to", pc)

    

