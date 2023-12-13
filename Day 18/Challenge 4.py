from turtle import Turtle, Screen
import random

screen = Screen()

screen.colormode(255)

def random_walk():
    positions = [90, 180, 360]
    tetitas = Turtle()
    tetitas.width(20)
    while True:
        paleta = random.sample(range(1, 255), 3)
        tetitas.color(paleta[0], paleta[1], paleta[2])
        tetitas.right(random.choice(positions))
        tetitas.forward(50)

random_walk()
screen.exitonclick()
