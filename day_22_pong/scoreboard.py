from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 30, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.player_1_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.player_2_score, align=ALIGNMENT, font=FONT)

    def player_one_point(self):
        self.player_1_score += 1
        self.update_scoreboard()

    def player_two_point(self):
        self.player_1_score += 1
        self.update_scoreboard()