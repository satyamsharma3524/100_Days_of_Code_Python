import turtle, random

timmy = turtle.Turtle()
screen = turtle.Screen()


def set_point(x,y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()


shape_side = 4
colours = ["red", "green", "blue", "orange", "brown", "purple", "red"]
set_point(0, 100)
count = 0

while shape_side <= 10:
    angle = 360/shape_side
    for _ in range(shape_side):
        timmy.forward(100)
        timmy.right(angle)
    shape_side += 1
    timmy.color(colours[count])
    count += 1


screen.exitonclick()
