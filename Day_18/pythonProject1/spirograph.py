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

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading+size_of_gap)
        tim.circle(100)

draw_spirograph(5)


screen.exitonclick()
