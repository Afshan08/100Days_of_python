import turtle as t
import random as rd
t.colormode(255)
screen = t.Screen()
tim = t.Turtle()


def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color


angles = [0, 180, 90, 270]
for _ in range(200):
    tim.width(15)
    angle = rd.choice(angles)
    color = random_color()
    tim.color(color)
    tim.speed("fastest")
    tim.setheading(angle)
    tim.forward(20)


screen.exitonclick()