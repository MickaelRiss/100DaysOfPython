from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score is {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.show()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGNMENT, font=FONT)
