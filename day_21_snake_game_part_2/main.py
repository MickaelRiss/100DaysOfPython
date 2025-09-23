import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkeypress(snake.turn_up, "Up")
screen.onkeypress(snake.turn_down, "Down")
screen.onkeypress(snake.turn_left, "Left")
screen.onkeypress(snake.turn_right, "Right")

game_on = True
screen.listen()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # If we touch the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # If we touch the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Did we touch tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()