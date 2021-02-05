from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 17, "bold")
GO_FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=GO_FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
