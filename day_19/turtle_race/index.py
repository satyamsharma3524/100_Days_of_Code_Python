import turtle
import random

screen = turtle.Screen()
is_race_on = False
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "pink", "yellow", "purple"]
y_position = [140, 80, 20, -40, -100, -160]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! the {winning_color} turtle is the winner.")
            else:
                print(f"You Lose! the {winning_color} turtle is the winner.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
