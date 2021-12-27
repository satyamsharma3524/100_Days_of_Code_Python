import random
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.width(2)
timmy.speed("fastest")

def draw_circle(radius):
    timmy.circle(radius)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(50):
    timmy.left(10)
    draw_circle(80)
    timmy.color(random_color())

screen.exitonclick()