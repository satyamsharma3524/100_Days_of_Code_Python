import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.title("India State game")

shape = "india_map.gif"

screen.addshape(shape)
timmy.shape(shape)

screen.exitonclick()
