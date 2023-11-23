# Beksultan
# 11/22/2023

# This program draws a polygon with the user`s parameters

import turtle

side = int(input('Enter how many sides your polygon should be: '))
length = int(input('Enter the length of each side: '))
color = input('Enter the color of the lines:  ')
fill_color = input('Enter the fill color: ')

polygon_turtle = turtle.Turtle()

polygon_turtle.pencolor(color)
polygon_turtle.fillcolor(fill_color)

polygon_turtle.begin_fill()

for _ in range(side):
    polygon_turtle.forward(length)
    polygon_turtle.left(360 / side)

polygon_turtle.end_fill()

turtle.done()
