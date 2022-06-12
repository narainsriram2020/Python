# Python Lord of the Rings
#
# Description: Mini-game themed on Lord of the Rings
#
# Author: Narain Sriram

import time
import random

print("Hello! Welcome to the Python Lord of the Rings game. This    game has very simple rules: I will display a character that  you have to get past by completing tasks. A timer will start when you begin so try to finish as early as possible! Good   luck!")
input("Please enter something to start ") 
t0 = time.time()
# The code above is for welcoming the user into the program and to make them press something to start the program. Once they start the program the time will start

# array of character prints
characters = ["           ___\n         .';:;'.\n        /_' _' /\   __\n        ;a/ e= J/-'\"  '.\n        \ ~_   (  -'  ( ;_ ,.\n         L~\"'_.    -.  \ ./  )\n         ,'-' '-._  _;  )'   (\n       .' .'   _.'\")  \  \(  |\n      /  (  .-'   __\{`', \  |\n     / .'  /  _.-'   \"  ; /  |\n    / /    '-._'-,     / / \ (\n __/ (_    ,;' .-'    / /  /_'-._\n`\"-'` ~`  ccc.'    __.','     \j\L\\\n                 .='/|\7      \n                   ' `","         /^\\\n    /\   \"V\"\n   /__\   I\n  //..\\\  I\n  \].`[/  I\n  /l\/j\  (]\n /. ~~ ,\/I\n \\\L__j^\/I\n  \/--v}  I\n  |    |  I\n  |    |  I\n  |    l  I\n_/j  L l\_!"," <>=======() \n(/\___   /|\\\          ()==========<>_\n      \_/ | \\\        //|\   ______/ \)\n        \_|  \\\      // | \_/\n          \|\/|\_   //  /\/\n           (oo)\ \_//  /\n          //_/\_\/ /  |\n         @@/  |=\  \  |\n              \_=\_ \ |\n                \==\ \|\_    \n             __(\===\(  )\\\n            (((~) __(_/   |\n                 (((~) \  /\n                 ______/ /\n                 '------'", "     _ .-'\n     _`\`\n `._/` ;_.  \,\n    `. /  _ /`\n      ;_ _,;\n    _/ , , /_,\n    `\"\ _  |'\n    _=}  ` ;/\n   .'    `. `-._\n,_/ ,| '    {  `.\n ] ',/  ; , ;\ , \_\n `._L`\  `  \ `.` :`\n  `\"` | / ; [   J./_\n     /   .   `. ` `\"\n    { ;' |\`._ \\\n    | `  ; J  ` \\\n   /_\_/__}{_\_/_)"]
#print(charcters[2])
start = time.time() # start timer
Gollum = 0
Gandalf = 0
Smaug = 0
list_vowel = ["a", "e", "i", "o", "u"]
previous_vowel = "b"
# These are all the variables in my code. They are used at various areas throughout my code

for i in range(10): # This is the for stateement that my whole code is in. It says ten so that the program can repeat ten times
    ran_char = random.randrange(0,3)
    # I have my random.randrange variable above to generate the random value on which character the user will receive

    if ran_char == 1:
        print(characters[1])
        print("This is Gandalf and he requires you to enter the phrase YOU SHALL NOT PASS if you want to go through!")
        gand_ans = input("Please enter your answer:")
        gand_ans = gand_ans.upper()
        if gand_ans == "YOU SHALL NOT PASS":
            print("Correct")
        else:
            print("That isn't correct!")
            break
    # The code above is meant for Gandolf. He requires the user to enter "You shall not pass" if they would like to go through. i made sure the set the input in the answer to upper so that it would be easier to check afterwards. 


    if ran_char == 0:
        print(characters[0])
        print("This is Gollum and he requires you to enter any vowel to move past. However once you use a vowel you cannot use it again")
        gol_ans = input("Please enter your answer:")
        gol_ans = gol_ans.lower()
        if gol_ans in list_vowel and gol_ans != previous_vowel:
            print("Correct")
            previous_vowel = gol_ans
        else:
            print("That isn't correct!")
            break
        # The code above is meant for Gollum who demnds a vowel to be eneterd by the user, if they would like to pass. I first had the input where the user would enter their vowel and then I made a variable equivalent to that input. 
        # This variable was then put through an if statement where the code questions whether it is a vowel. I had a premade list containing vowels so the code puts the input into a check through that. Then iif that is correct, the previous_vowel vraiable is stored at the latest answer. Now the same vowel cannot be entered into the program the next time.

    if ran_char == 2:
        print(characters[2])
        print("This is Smaug and he requires payment to be defeated. Please pay in American denominations")
        ran_sma = random.randrange(0,1001)
        print("Smaug needs you to pay", ran_sma, "if you want to pass")
        hun_mon = int(input("How many $100:"))
        fif_mon = int(input("How many $50:"))
        twe_mon = int(input("How many $20:"))
        ten_mon = int(input("How many $10:"))
        fiv_mon = int(input("How many $5:"))
        one_mon = int(input("How many $1:"))
        total = (hun_mon * 100) + (fif_mon * 50) + (twe_mon * 20) + (ten_mon * 10) + (fiv_mon * 5) + (one_mon * 1)
        print(total)
        if total == ran_sma:
            print("Correct")
        else:
            print("That's not correct!")
            break
    # This piece of code is meant for Smaug. I first created a random number whicb was the value the user had to enter. There were 6 different denominations in which the user could pay and I made 6 different variables. These variables where then multiplied by their respective values (Tens would be multiplied with 10).
    # Then I created a total variable which is a sum of the individual values. This is then put through an if statement that checks to see whether the random number is the same value as the total variable

t1 = time.time()   # This stops my timer 
time = t1-t0 # Meant to subtract the end time with the starting time
print("Game Over")
print("Your time is:", time)
# I have a print statement at the end displaying "Game Over" and showing how long it took the user to complete the program