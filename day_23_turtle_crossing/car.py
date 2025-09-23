from turtle import Turtle
import random

CAR_COLOR = ["yellow", "red", "green", "blue", "pink", "purple", "OliveDrab"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(CAR_COLOR))
        self.setheading(180)
        self.set_position()
        self.car_speed = 0
        self.acceleration(1)

    def set_position(self):
        y_value = random.randint(-250, 250)
        self.goto(310, y_value)

    def move(self):
        self.forward(self.car_speed)

    def acceleration(self, increase):
        self.car_speed = (MOVE_INCREMENT * increase)