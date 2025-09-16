import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race ? Please enter a color: ")
colors = ["purple", "red", "green", "yellow", "blue", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0, 6):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=-y_positions[index])
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congratulation you've won! The winner is {winner}.")
            else:
                print(f"Sorry... you've lost! The winner is {winner}.")

screen.exitonclick()