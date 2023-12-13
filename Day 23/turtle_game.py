from turtle import Screen
from turtle_class import Turtle_Cross
from car_class import Car_barrage
from scoreboard_class import Scoreboard
import random as rd
import time

screen = Screen()
screen.tracer(0)
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("white")

cars = Car_barrage()

turtle = Turtle_Cross()

screen.onkeypress(turtle.move, "Up")
screen.listen()
screen.update()

scoreboard = Scoreboard()

counter = 2
level = 1
score = 0
game_status = True

while game_status:
    if counter % 2 == 0:
        cars.create_car(level)
    for car in cars.car_list:
        if car.distance(turtle) < 25:
            game_status = False
            print("GAME OVER")
    if turtle.at_end():
        turtle.reser_turtle()
        level += 1
        score += 1
    scoreboard.draw_score(score)
    time.sleep(0.1)
    cars.move_barrage()
    counter += 0.5
    screen.update()

screen.exitonclick
