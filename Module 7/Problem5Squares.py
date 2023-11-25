# Beksultan
# 11/25/2023

# This is a problem #5 and this program draw a squares inside the square.

import turtle

def draw_square(t, a, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.backward(a // 2)
    t.setheading(0)
    t.backward(a // 2)
    t.pendown()

    for _ in range(4):
        t.forward(a)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color('blue')

# Draw squares similar to the other code
draw_square(alex, 20, 0, 0)
draw_square(alex, 50, 0, 0)
draw_square(alex, 70, 0, 0)
draw_square(alex, 90, 0, 0)
draw_square(alex, 110, 0, 0)

wn.exitonclick()