import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

pong_1 = Paddle(350, 0)
pong_2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0, 0)
screen.listen()


screen.onkey(fun=pong_1.up, key="Up")
screen.onkey(fun=pong_1.down, key="Down")
screen.onkey(fun=pong_2.up, key="w")
screen.onkey(fun=pong_2.down, key="s")


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddle
    if ball.xcor() > 320 and ball.distance(pong_1) < 50 or ball.xcor() < -320 and ball.distance(pong_2) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_1()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_2()

screen.exitonclick()
