from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="left", font=FONT)
