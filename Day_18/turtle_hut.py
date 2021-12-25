import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def set_point(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()


def triangle(side):

    for _ in range(3):
        timmy.forward(side)
        timmy.left(120)


def square(side):
    for _ in range(4):
        timmy.forward(side)
        timmy.right(90)


def rectangle(x_side, y_side):
    for _ in range(2):
        timmy.forward(x_side)
        timmy.right(90)
        timmy.forward(y_side)
        timmy.right(90)


def paralellogram(x_side, y_side):
    for _ in range(2):
        timmy.forward(x_side)
        timmy.right(60)
        timmy.forward(y_side)
        timmy.right(120)


def hut():
    set_point(-300, 100)
    triangle(100)
    rectangle(100, 200)
    set_point(-250, 187)
    paralellogram(200, 100)
    set_point(-200, 100)
    square(200)
    set_point(-150, 50)
    square(80)
    set_point(-297, 90)
    rectangle(90, 180)


hut()
screen.exitonclick()
