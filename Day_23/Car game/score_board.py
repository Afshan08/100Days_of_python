from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-230, 250)
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
