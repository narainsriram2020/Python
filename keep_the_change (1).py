# Python Keep the Change
#
# Program that divides a monetary amount in change
#
# Author: Narain Sriram
#

Total = float(input("Please enter the monetary amount: "))
print("")
New_Total = Total * 100


Quarters = 25
Dimes = 10
Nickels = 5
Pennies = 1


A = New_Total//Quarters
B = (New_Total-A*25)//Dimes
C = (New_Total-(A*25+B*10))//Nickels
D = (New_Total-(A*25+B*10+C*5))//Pennies


print("The change required to make $", Total, " is:")
A = int(A)
print("Quarters:", A)
B = int(B)
print("Dimes:   ", B)
C = int(C)
print("Nickels: ", C)
D = int(D)
print("Pennies: ", D)
