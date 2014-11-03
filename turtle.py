# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 3 - Problem 4
# Purpose: draw a shape using number of sides and length as input
# Input: N/A
# Output: N/A

import turtle
# asks how many sides the shape should have
sides = int(raw_input('How many sides would you like the shape to have? '))
# asks how long the sides should be
length = int(raw_input('How long would you like each side to be? '))
print "Waking up the turtle..."
# opens a window
window = turtle.Screen()
# creates a turtle named Burt
Burt = turtle.Turtle()
# calculation for turn angle using sides input
angle = (180-(180*(sides-2)/sides))
# for loop for completing the shape
for side in range(sides):
	Burt.forward(length)
	Burt.left(angle)