from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0


    def update_score_board(self):
        self.clear()
        self.goto(-100, 198)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 198)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))


    def l_scores(self):
        self.l_score += 1


    def r_scores(self):
        self.r_score += 1