import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
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

screen.exitonclick()
