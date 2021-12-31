import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    timmy.forward(10)

def move_left():
    timmy.left(10)

def move_right():
    timmy.right(10)

def move_back():
    timmy.back(10)


screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Down", fun=move_back)
screen.onkey(key="c", fun=turtle.resetscreen)

screen.exitonclick()
