# Python Turtle Drawing
#
# Drawing Sports Car with Python Turtle
#
# Author: Narain Sriram
# https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()
x = 1

# Turn the pen to Blue
t.pencolor("Blue")
turtle.position()
t.goto(-22,0)
t.forward(x * 90)
t.left(60)
t.end_fill()
# Turn the pen to yellow for the tires
t.pencolor("Yellow")
# Method for the top part of tire
def tire_curve():
    for i in range(58):
        t.right(2)
        t.forward(x * 1)

# Back tire
t.fillcolor("Yellow")
t.begin_fill()
t.circle(x * -30)
tire_curve()
t.left(55)
t.end_fill()

# Back end of car
t.pencolor("Blue")
t.forward(x * 50)
t.left(35)
t.forward(x * 40)
t.left(56)
t.forward(x * 100)

# Spoiler
t.left(165)
t.forward(x * 30)

# Back Plane and Roof
t.right(100)
t.forward(x * 100)
t.left(25)
t.forward(x * 140)

# Front Windshield
t.pencolor("Red")
t.left(30)
t.forward(x * 90)

# Hood
t.right(30)
t.forward(x * 50)

def front_curve():
    for i in range(45):
        t.left(2)
        t.forward(x * 1)

# Front bumper
front_curve()
t.forward(x * 60)
t.left(90)

# Bottom Engine
t.forward(x * 65)
t.right(120)

# Front Tire
t.pencolor("Yellow")
t.fillcolor("Yellow")
t.begin_fill()
def tire_curve1():
    for i in range(120):
        t.left(2)
        t.forward(x * 1)
t.circle(x * 30)
tire_curve1()
t.end_fill()
t.pencolor("Blue")
t.right(122)
t.forward(x * 60)

# Start of code to create the fill of the first end of the car
t.fillcolor("Red")
t.begin_fill()
t.left(99)
t.forward(x * 138)
t.left(83)

# Retracing to color in the first part
# Front Windshield
t.pencolor("Red")
t.left(30)
t.forward(x * 90)

# Hood
t.right(30)
t.forward(x * 50)

def front_curve():
    for i in range(45):
        t.left(2)
        t.forward(x * 1)

# Front bumper
front_curve()
t.forward(x * 60)
t.left(90)

# Bottom Engine
t.forward(x * 65)
t.right(120)
t.end_fill()

# Front Tire
t.pencolor("Yellow")
t.fillcolor("Yellow")
t.begin_fill()
def tire_curve1():
    for i in range(120):
        t.left(2)
        t.forward(x * 1)
t.circle(x * 30)
tire_curve1()
t.end_fill()
# End fill of Red first part of Car



t.shapesize(1.0, 1.0, 1)