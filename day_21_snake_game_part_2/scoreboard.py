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
        self.high_score = 0
        self.retrieve_save()
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score : {self.score} | High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.show()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def save_score(self):
        score = str(self.high_score)
        with open("saving.txt", mode="w") as f:
            f.write(score)

    def retrieve_save(self):
        with open("saving.txt", mode="r") as f:
            score = f.read()
            self.high_score = int(score)