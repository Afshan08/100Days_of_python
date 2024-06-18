from turtle import Turtle, Screen
import random as rd

color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = 5
INCREASE_MOVE = 10


class CarManger:

    def __init__(self):
        self.car_list = []  # List to store the car objects
        self.create_cars()  # Call the method to create cars
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 1:
            car = Turtle()  # Create a new Turtle object for each car
            car.shape("square")  # Set the shape to square
            car.shapesize(stretch_len=2)  # Stretch the shape to look like a car
            car.color(rd.choice(color))  # Randomly choose a color from the colors list
            y = rd.randint(-250, 250)  # Randomly choose a y position
            car.penup()  # Lift the pen up so it doesn't draw
            car.goto(300, y)  # Set the position of the car
            self.car_list.append(car)  # Add the car to the car list

    def move_cars(self):
        for cars in self.car_list:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREASE_MOVE

