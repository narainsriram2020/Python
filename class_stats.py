# Python Class Stats
#
# arrays with survey responses--items at the same index are from the same individual
#
# Author: Narain Sriram

seasons = ['Fall', 'Winter', 'Summer', 'Winter', 'Summer', 'Fall', 'Summer', 'Winter', 'Summer', 'Winter', 'Spring', 'Winter', 'Spring', 'Summer', 'Fall', 'Spring', 'Summer', 'Fall', 'Summer', 'Winter', 'Spring', 'Winter', 'Fall', 'Summer', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Winter', 'Summer', 'Spring', 'Winter', 'Summer', 'Fall', 'Fall', 'Fall', 'Winter', 'Spring', 'Spring', 'Summer', 'Spring', 'Fall', 'Summer', 'Winter', 'Fall', 'Winter', 'Fall', 'Summer', 'Summer', 'Spring', 'Fall', 'Spring', 'Summer', 'Winter', 'Winter', 'Summer', 'Winter', 'Summer', 'Spring', 'Winter', 'Fall', 'Summer', 'Spring', 'Fall', 'Summer', 'Winter', 'Winter', 'Winter', 'Winter', 'Winter', 'Fall', 'Winter']
shows = [4, 0, 1, 5, 2, 5, 2, 3, 8, 1, 0, 2, 10, 2, 1, 1, 2, 2, 3, 0, 0, 0, 0, 0, 2, 2, 3, 0, 1, 1, 3, 2, 2, 1, 2, 0, 2, 2, 1, 0, 1, 2, 2, 4, 2, 1, 1, 5, 3, 0, 3, 1, 0, 2, 3, 3, 0, 2, 1, 0, 2, 0, 4, 1, 2, 3, 4, 0, 3, 1, 2, 2, 0, 0]
months = ['May', 'May', 'January', 'September', 'February', 'April', 'April', 'June', 'August', 'June', 'March', 'May', 'April', 'August', 'August', 'October', 'October', 'September', 'October', 'September', 'May', 'January', 'September', 'August', 'February', 'May', 'December', 'July', 'July', 'September', 'January', 'June', 'September', 'December', 'July', 'May', 'December', 'August', 'November', 'August', 'May', 'June', 'September', 'June', 'March', 'August', 'October', 'May', 'July', 'May', 'February', 'April', 'May', 'February', 'November', 'September', 'January', 'April', 'September', 'January', 'May', 'July', 'January', 'August', 'February', 'September', 'September', 'January', 'March', 'July', 'September', 'May', 'May', 'September']
days = [9, 30, 2, 21, 20, 20, 8, 5, 20, 25, 27, 16, 10, 14, 13, 9, 17, 15, 9, 22, 21, 13, 15, 10, 11, 31, 19, 5, 5, 23, 2, 17, 11, 20, 15, 18, 31, 17, 8, 5, 9, 17, 10, 23, 16, 2, 15, 8, 10, 18, 8, 24, 1, 15, 24, 9, 1, 18, 26, 6, 16, 6, 3, 30, 6, 11, 14, 23, 1, 23, 1, 16, 24, 27]

# The following code is for the first step of the assignment: finding the number of students preferring different seasons. 
# These are 4 variables representing each season
Winter = 0 
Spring = 0
Summer = 0
Fall = 0
# In the for loop, I am using an if statement and analyzing the list to find each season
# Adding += 1 to each time I find the season in the list
for i in seasons:
    if i == 'Winter':
        Winter += 1
    if i == 'Spring':
        Spring += 1
    if i == 'Summer':
        Summer += 1
    if i == 'Fall':
        Fall += 1
# Print out the function at the end with the total number (Which is the variable)
print("Number of students preferring Winter:", Winter)
print("Number of students preferring Spring:", Spring)
print("Number of students preferring Summer:", Summer)
print("Number of students preferring Fall:", Fall)
print()

# Second part of the assignment: Average number of shows watched
num_add = 0 # Set the varuable to 0
for i in shows: # The for loop adds all the numbers in the list
    num_add = num_add + i
avg = num_add / len(shows) # Taking the total and dividing it by the number of numbers in the list
print("Average number of shows watched:", avg)
print()

# Third part of the assignment: Determine if someone was born on leap day
leap = True
for i in range(len(months)):
    if months[i] == "Feburary":
        if days[i] == 29:
            leap = True
    else:
        leap = False

print("A student was born on leap day:", leap)
    



