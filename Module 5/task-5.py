# Beksultan
# 11/22/2023

# This program draw a some kind of picture

import turtle

screen = turtle.Screen()
screen.bgcolor('white')

pen = turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.pensize(1)

def draw_hexagon():
    for _ in range(6):
        pen.forward(50)
        pen.left(60)

for _ in range(9):
    draw_hexagon()
    pen.left(45)

turtle.done()