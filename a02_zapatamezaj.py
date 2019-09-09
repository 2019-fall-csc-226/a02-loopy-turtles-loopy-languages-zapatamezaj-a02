######################################################################
# Author: Jose Zapata Meza
# Username: zapatamezaj

# Assignment: A02: Loopy Turtle, Loopy Languages
# Purpose: Practice using the turtle library and loops
######################################################################
# Acknowledgements:

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
# Imports the turtle files
import turtle

# Creates a window with a grey background
wn = turtle.Screen()
wn.bgcolor("grey")

# Creates a turtle that is named Jose
jose = turtle.Turtle()
jose.setheading(0)

# Jose's color is blue
jose.color('blue')

# The origin of Jose is moved
jose.penup()
jose.back(200)
jose.pendown()

# A turtle to make a road is created and placed to where the road should be
road = turtle.Turtle()
road.penup()
road.backward(340)
road.right(90)
road.forward(150)
road.left(90)
road.pendown()
road.forward(700)

# A turtle to draw a sun is created
sun = turtle.Turtle()
sun.penup()
sun.color('yellow')
sun.forward(250)
sun.left(90)
sun.forward(220)
sun.pendown()

# The turtle fills its shape to make the sun bright
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.hideturtle()

# A loop is created to draw a rectangle
for i in range(2):
        jose.forward(400)
        jose.right(90)
        jose.forward(100)
        jose.right(90)

# Jose moves to draw the rear tire of the car
jose.forward(50)
jose.penup()
jose.right(90)
jose.forward(100)
jose.pendown()
jose.circle(50)

# Jose moves to draw the front tire of the car
jose.left(90)
jose.forward(200)
jose.right(90)
jose.circle(50)

# Jose moves to make the top part of the car
jose.left(90)
jose.forward(100)
jose.left(90)
jose.penup()
jose.forward(100)
jose.pendown()
jose.forward(100)
jose.left(90)
jose.forward(300)
jose.left(90)
jose.forward(100)

jose.hideturtle()

# To end the program, one clicks on the screen
wn.exitonclick()
