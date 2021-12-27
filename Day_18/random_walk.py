import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.speed("fastest")
timmy.width(10)

directions = [0, 90, 180, 270]

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

while True:
    timmy.setheading(random.choice(directions))
    timmy.color(random_colors())
    timmy.forward(30)


screen.exitonclick()
