import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.color("blue", "yellow")

timmy.begin_fill()

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

timmy.end_fill()
screen.exitonclick()