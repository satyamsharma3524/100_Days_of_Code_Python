import turtle

timmy = turtle.Turtle()


def set_point(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()


set_point(-300, 0)
for _ in range(30):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = turtle.Screen()
screen.exitonclick()