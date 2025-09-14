from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("forest green")

for _ in range(20):
    timmy_turtle.pendown()
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)

screen = Screen()
screen.exitonclick()