# TODO 1: import important libraries
import time
import turtle
from turtle import Turtle, Screen
import time
from player import Player
from car import CarManger
from score_board import ScoreBoard



# TODO 2: make the screen by using the screen module

screen = Screen()
screen.title("Car Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManger()
player = Player()
score_board = ScoreBoard()
screen.listen()
screen.onkey(player.goup, "Up")
# TODO 3: create a while loop while game is on variable is true
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # detect collision wit cars
    for cars in car_manager.car_list:
        if cars.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()



screen.exitonclick()