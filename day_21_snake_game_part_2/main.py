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
        snake.extend()
        score.update()
        food.refresh()

    # If we touch the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Did we touch tail
    for segment in snake.segments[1:]:
        if segment.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()