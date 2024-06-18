from turtle import Turtle


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)
        if self.ycor() > 280 or self.ycor() < -280:
            self.bouncey()


    def bouncey(self):
        self.y_move *= -1


    def bouncex(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def rest_ball(self):
        self.goto(0, 0)
        self.bouncex()






