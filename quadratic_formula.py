# Quadratic Formula
#
# Description: Quadratiic Formula Calculator
#
# Author: Narain Sriram
#

print("Hello, welcome to the Quadratic Formula solver")
print("The equation should look like the following: -b +/- ((b*b - 4*a*c) ** 0.5) / 2 * a")
a = float(input("Please enter your a variable: "))
b = float(input("Please enter you a variable: "))
c = float(input("Please enter your a variable: "))
dis = ((b*b - 4*a*c) **0.5)
if dis == 0:
    print("No real roots")
    
else:
    x1 = (-b - dis) / 2 * a 
    x2 = (-b + dis) / 2 * a
    print("The roots of the equation are at x =", x1,  "and", x2)


