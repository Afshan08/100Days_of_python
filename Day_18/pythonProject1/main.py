sfrom turtle import Turtle, Screen
import random as rd

screen = Screen()
tim = Turtle()
colors = ["red", "blue", "green", "orange", "blue1", "red", "blue", "yellow", "green",]



def making_shapes(maximum_sides, color):
    x = 3
    while x != maximum_sides:
        tu = rd.choice(color)
        for _ in range(x):
            tim.color(tu)
            tim.forward(100)
            tim.right(360/x)
        x += 1


making_shapes(10, colors)
screen.exitonclick()

