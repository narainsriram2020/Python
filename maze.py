# Python Maze
#
# Maze the the user had to go through
#
# Author: Narain Sriram

# maze creation - start at S
#               - goal is G
#               - spaces are paths
#               - X's are walls
maze1 = [['X','S','X','X','X','X','X','X','X','X'], ['X',' ',' ',' ',' ',' ',' ',' ',' ','X'], ['X',' ','X','X','X',' ','X',' ','X','X'], ['X',' ','X',' ','X',' ','X',' ',' ','X'], ['X',' ',' ',' ','X',' ','X','X','X','X'], ['X',' ','X','X','X',' ',' ',' ',' ','X'], ['X',' ',' ',' ','X',' ','X','X',' ','X'], ['X',' ','X',' ','X',' ','X',' ',' ','X'], ['X',' ',' ',' ','X',' ','X',' ','X','X'], ['X','X','X','X','X','X','X','G','X','X']]
maze2 = [['X','X','X','X','X','X','X','X','X','X'], ['X',' ',' ',' ',' ',' ',' ',' ',' ','X'], ['X',' ','X','X','X',' ','X',' ','X','X'], ['X',' ','X',' ','X',' ','X',' ',' ','X'], ['X',' ',' ',' ','X',' ','X','X','X','X'], ['X',' ','X','X','X',' ',' ',' ',' ','X'], ['X',' ',' ',' ','X',' ','X','X',' ','X'], ['X',' ','X',' ','X',' ','X',' ',' ','X'], ['X',' ',' ',' ','X',' ','X','S','X','X'], ['X','X','X','X','X','X','X','G','X','X']]

maze3 = [['X','S','X','X','X','X','X','X','X','X'], ['X',' ','X',' ',' ',' ',' ',' ',' ','X'], ['X',' ','X',' ','X','X','X','X','X','X'], ['X',' ',' ',' ',' ',' ',' ',' ',' ','X'], ['X','X','X','X','X',' ','X','X',' ','X'], ['X',' ',' ',' ','X',' ',' ',' ','X','X'], ['X',' ','X',' ','X','X','X',' ','X','X'], ['X','X','X',' ','X','X','X',' ',' ','X'], ['X',' ',' ',' ',' ',' ',' ',' ','X','X'], ['X','G','X','X','X','X','X','X','X','X']]

# statement to select whichever maze you'd like
maze = maze2

# the loop below is particularly useful for nicely printing the maze, but modify as desired
# Below is my intro statement
print("Hello, welcome to my maze game! In this game you start at S. The X is the walls, and the spaces between the walls are the places you can go to. Finally, your     final goal is to get to G. Good Luck!")

# The following are my variables that used in various places
Current_R = 0
Current_C = 0
finish_Row = 0
finish_Col = 0

# Find the Row and Column of the maze
for rowIndex in range(len(maze)): # row = maze[0]
    for colIndex in range(len(maze[rowIndex])): # item = row[0]
    # Set up my S, P and G
        if maze[rowIndex][colIndex] == "S":
            Current_R = rowIndex
            Current_C = colIndex
            maze[rowIndex][colIndex] = "P"
        if maze[rowIndex][colIndex] == "G":
            finish_Row = rowIndex
            finish_Col = colIndex


while True:
    for row in maze:
        for element in row:
            print(element, end = " ")
        print()
        # Ask the user where htey would like to move
    user_move = input("Please enter your move: ")

# If the user enters something other than a designated move, then it is coined as invalid
    if user_move != "up" and  user_move != "down" and  user_move != "left" and  user_move != "right":
        print("Invalid move...")
        print()

# The following code is for the down feature
    elif user_move == "down":

        # If there is a X where the P is trying to move, it will be an invalid move
        if Current_R == 10:
            print("Out of Bounds")
            Current_R -= 1
        if maze[Current_R + 1][Current_C] == "X" or maze[Current_R + 1][Current_C] == "S":
            print("Invalid Move")

        elif maze[Current_R + 1][Current_C] != "X" and maze[Current_R + 1][Current_C] != "S":
            # Change to P 
            maze[Current_R + 1][Current_C] = "P"
            maze[Current_R][Current_C] = " "
            Current_R += 1
            print()
                   
    # Feature for up movement
    elif user_move == "up":

        if Current_R == -1:
            ("Invalid Move")
            Current_R += 1
         # If there is a X where the P is trying to move, it will be an invalid move
        if maze[Current_R - 1][Current_C] == "X" or maze[Current_R + 1][Current_C] == "S":
            print("Invalid Move")

        if maze[Current_R - 1][Current_C] != "X" and maze[Current_R + 1][Current_C] != "S":
            maze[Current_R - 1][Current_C] = "P"
            maze[Current_R][Current_C] = " "
            Current_R -= 1
            print()


    elif user_move == "left":

        if Current_C == -1:
            print("Invalid Move")
            Current_C += 1
        if maze[Current_R][Current_C - 1] != "X" and maze[Current_R + 1][Current_C] != "S":
            maze[Current_R][Current_C - 1] = "P"
            maze[Current_R][Current_C] = " "
            Current_C -= 1
            print()

            # If there is a X where the P is trying to move, it will be an invalid move
        if maze[Current_R][Current_C - 1] == "X" or maze[Current_R + 1][Current_C] == "S":
            print("Invalid Move")


# This is the function to move right 
    elif user_move == "right":

        if Current_C == 10:
            print("Invalid Move")
            Current_C -= 1

        # This is the code P to move right
        if maze[Current_R][Current_C + 1] != "X" and maze[Current_R + 1][Current_C] != "S":
            maze[Current_R][Current_C + 1] = "P"
            maze[Current_R][Current_C] = " "
            Current_C += 1
            print()
            
            # If there is a X where the P is trying to move, it will be an invalid move
        if maze[Current_R][Current_C + 1] == "X" or maze[Current_R + 1][Current_C] == "S":
            print("Invalid Move")

# This code is used to measure when the user completes the program and will display "You Win!" if they get to G
    if Current_R == finish_Row and Current_C == finish_Col:
        print("You Win")
        break

        

