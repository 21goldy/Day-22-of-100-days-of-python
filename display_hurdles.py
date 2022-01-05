from turtle import Turtle
import random

COLORS = ['blue', 'red', 'yellow', 'lightpink', 'deep sky blue', 'orange', 'green', 'brown']

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class Hurdles:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_manager(self):
        random_chances = random.randint(1, 6)
        if random_chances == 1:
            random_colors = random.choice(COLORS)
            tim = Turtle(shape='square')
            tim.penup()
            tim.speed('fastest')
            tim.shapesize(1, 2)
            tim.penup()
            tim.color(random_colors)
            random_x = random.randint(-250, 280)
            random_y = random.randint(-250, 280)
            tim.goto(random_x, random_y)
            self.cars.append(tim)

    def move_cars(self):
        for car in self.cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
