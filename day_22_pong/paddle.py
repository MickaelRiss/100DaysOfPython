from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, player = 1):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.player_position(player)

    def player_position(self, player_num = 1):
        self.goto(350, 0) if player_num == 1 else self.goto(-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)