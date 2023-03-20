from turtle import Screen
from paddle import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My-Pong-Game")
screen.tracer(0)

paddle1 = Paddles(360, 0)
paddle2 = Paddles(-370, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # detect collision with paddles
    if ball.xcor() > 330 and ball.distance(paddle1) < 60 or ball.xcor() < -340 and ball.distance(paddle2) < 50:
        ball.bounce_x()

    # detect collision with right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p1_point()

    # detect collision with left wall
    if ball.xcor() < -387:
        ball.reset_position()
        scoreboard.p2_point()








screen.exitonclick()
