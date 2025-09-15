import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("forest green")
colors = ["cornflower blue","midnight blue","midnight blue","medium sea green","medium sea green","dark green","light yellow","dark khaki","gold","peru","saddle brown","navajo white","light salmon","orange red","red","hot pink","purple","thistle","blue violet"]
directions = [0, 90, 180, 270]
timmy.pensize(1)
timmy.speed(0)

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.left(angle)
#         timmy.forward(100)
#
# for shape_side_n in range (3, 11):
#     timmy.color(random.choice(colors))
#     draw_shapes(shape_side_n)

def generate_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    color = (r, g, b)
    return color
#
# for _ in range(20):
#     timmy.circle(50)
#     timmy.color(generate_color())
#     timmy.forward(100)
#     timmy.setheading(random.choice(directions))

r = 100 # radius

for i in range(360):
    if i % 10 == 0:
        timmy.color(generate_color())
        timmy.setheading(i+10)
        timmy.circle(r)

screen = t.Screen()
screen.exitonclick()