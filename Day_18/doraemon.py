import turtle

doraemon = turtle.Turtle()
screen = turtle.Screen()


def draw_circle(radius):
    doraemon.circle(radius)


draw_circle(100)
draw_circle(80)

screen.exitonclick()