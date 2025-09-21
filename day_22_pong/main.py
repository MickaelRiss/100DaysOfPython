from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle(2)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() > -320 :
        ball.bounce_x()

    # Detect ball out
    if ball.xcor() > 380:
        score.player_two_point()
        ball.reset_position()

    if ball.xcor() < -380:
        score.player_one_point()
        ball.reset_position()

screen.exitonclick()
