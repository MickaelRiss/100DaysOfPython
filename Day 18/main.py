from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("forest green")
colors = ["cornflower blue","midnight blue","midnight blue","medium sea green","medium sea green","dark green","light yellow","dark khaki","gold","peru","saddle brown","navajo white","light salmon","orange red","red","hot pink","purple","thistle","blue violet"]

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.left(angle)
        timmy.forward(100)

for shape_side_n in range (3, 11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_side_n)

screen = Screen()
screen.exitonclick()