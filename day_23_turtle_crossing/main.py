import time
import turtle as t
from types import new_class

from player import Player
from car import Car
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_on = True
# I should create a car manager class instead of this array/list
car_list = []
i = 0

while game_on:
    time.sleep(0.1)
    screen.update()

    # Generate new car every 6 update
    if i % 6 == 0:
        new_car = Car()
        new_car.acceleration(score.level)
        car_list.append(new_car)

    # Detect top of the screen
    if player.position() == (0, 300):
        score.update_level()
        player.refresh_position()
        [car.acceleration(score.level) for car in car_list]

    # Move all the cars
    for car in car_list:
        car.move()
        # Detect contact with car
        if player.distance(car) < 20:
            score.game_over()
            game_on = False

    i += 1

screen.exitonclick()