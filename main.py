import turtle
from turtle import Screen
from command import Command
from display_hurdles import Hurdles
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title('Hurdle Race')
screen.setup(width=600, height=600)
screen.tracer()

c = Command()
h = Hurdles()
s = Scoreboard()
screen.listen()
screen.onkey(fun=c.up, key='Up')
screen.onkey(fun=c.down, key='Down')
screen.onkey(fun=c.up, key='w')
screen.onkey(fun=c.down, key='s')

is_on = True
while is_on:
    time.sleep(0.01)
    screen.update()

    h.car_manager()
    h.move_cars()

    for car in h.cars:
        if car.distance(c) < 35:
            s.game_over()
            is_on = False

    if c.is_at_finish_line():
        c.go_to_start()
        h.level_up()
        s.increase_level()

screen.exitonclick()
