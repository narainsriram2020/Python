# Python Since Y2K
#
# Description: Program that calculates the number of seconds since January 1, 2000
#
# Author: Narain Sriram

print("Hello, welcome to number of seconds since Y2K")
print("Please enter all your solutions through numbers")
print("")

year = int(input ("What year would you like to enter? (after 2000)\n"))
month = int(input ("What month of the year would you like to enter?( Out of 12)\n"))
day = int(input ("What day of the month would you like to enter?(out of 30)\n"))
hour = int(input ("What hour of the day would you like to enter?(Out of 24)\n"))
minute = int(input ("What minute of the hour would you like to enter?(Out of 60)\n"))
print("")

A = (year - 2000)*31104000
B = (month*2592000 )
C = (day*86400 )
D = (hour*3600 )
E = (minute*60 )

numbers_with_commas = "{:,}".format(A + B + C + D + E)
print("The entered date is", numbers_with_commas, "seconds past the start of the millennium")