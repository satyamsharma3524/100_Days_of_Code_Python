# we are going to use the turtle graphics library from python in this program
import turtle

# here timmy is the object created by the turtle class
timmy = turtle.Turtle()
my_screen = turtle.Screen()
timmy.shape("turtle")
timmy.color("blue")

while True:
    timmy.forward(100)
    timmy.left(90)


my_screen.exitonclick()
