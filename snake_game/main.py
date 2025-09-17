import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake = []
screen.tracer(0)

for position in starting_position:
    new_snake = t.Turtle("square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    snake.append(new_snake)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()
