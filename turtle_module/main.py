import turtle as t
import colorgram
import random

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]
t.colormode(255)
turtle = t.Turtle()
turtle.shape()
turtle.pensize(1)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

def draw_line():
    for _ in range(0, 10):
        turtle.pendown()
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.forward(50)

for i in range (0, 10):
    turtle.setpos(-100, -100 + (i * 50))
    draw_line()

screen = t.Screen()
screen.exitonclick()