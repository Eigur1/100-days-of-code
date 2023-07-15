import colorgram as cg
import random as rn
from turtle import Turtle, Screen
from math import (sqrt)


def generate_color_list(number_colors):
    colors = cg.extract('reference.jpg', number_colors)
    color_list = []
    for i in range(0, len(colors) - 1):
        actualcolor = colors[i]
        local_list = (actualcolor.rgb)[0], (actualcolor.rgb)[1], (actualcolor.rgb)[2]
        color_list.append(local_list)
    return color_list


def create_painting(num_of_dots, radius):
    screen = Screen()
    screen.colormode(255)
    pezon = Turtle()
    color_list = generate_color_list(num_of_dots)
    square_num = round(sqrt(num_of_dots))

    pezon.speed(12)
    pezon.penup()
    pezon.left(90)
    pezon.forward((2 * radius) * square_num)
    pezon.left(90)
    pezon.forward((2 * radius) * square_num)
    pezon.right(180)
    pezon.pendown()
    for t in range(square_num):
        for i in range(square_num):
            locar_color = rn.choice(color_list)
            pezon.color(locar_color)
            pezon.fillcolor(locar_color)
            pezon.begin_fill()
            pezon.circle(radius)
            pezon.end_fill()
            pezon.penup()
            pezon.forward(4 * radius)
            pezon.pendown()
        pezon.penup()
        pezon.right(180)
        pezon.forward((4 * radius) * square_num)
        pezon.left(90)
        pezon.forward(4 * radius)
        pezon.left(90)
    screen.exitonclick()


create_painting(200, 10)

generate_color_list(20)
