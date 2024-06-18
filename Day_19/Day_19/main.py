from turtle import Turtle, Screen

timm = Turtle()
screen = Screen()


def move_forwards():
    timm.forward(10)


def move_backwards():
    timm.backward(10)


def move_left():
    new_heading = timm.heading()+10
    timm.setheading(new_heading)


def move_right():
    new_heading = timm.heading()-10
    timm.setheading(new_heading)


def clear():
    timm.clear()
    timm.penup()
    timm.home()
    timm.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
