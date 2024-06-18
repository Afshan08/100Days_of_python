from turtle import Turtle, Screen
import random as rd
colors = ["red", "blue", "green", "yellow", "pink", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet.", "Which turtle will win the race?")
all_turtles = []
if user_bet:
    is_race_on = True
for turtle_index in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
print(user_bet)

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won, the winning turtle is {winning_color}")
            else:
                print(f"You have lost, the winning turtle is {winning_color}")

        distance_by = rd.randint(0, 10)
        turtle.forward(distance_by)



screen.exitonclick()

