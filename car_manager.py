from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(COLORS[randint(0, 5)])
            new_car.goto(x=300, y=randint(-250, 250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT

