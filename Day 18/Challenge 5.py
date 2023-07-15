from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


def draw_circle(gap):
    culito = Turtle()
    culito.speed(10)
    for i in range(0, 359):
        paleta = random.sample(range(1, 255), 3)
        culito.color(paleta[0], paleta[1], paleta[2])
        culito.circle(100)
        culito.setheading(culito.heading() + gap)


draw_circle(10)
screen = Screen()
screen.exitonclick()
