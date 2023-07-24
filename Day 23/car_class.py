from turtle import Turtle
import random as rd
import time

COLOR_LIST = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
              "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]


class Car_barrage():
    def __init__(self):
        super().__init__()
        car_list = []
        self.car_list = car_list


    def create_car(self, level):
        rn_ycor = rd.randint(-300, 300)
        car = Turtle()
        rd_speed = 3 + level*3 / 2
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.color(rd.choice(COLOR_LIST))
        car.goto(310, rn_ycor)
        car.speed(rd.uniform(3 + level, rd_speed))
        car.setheading(180)
        self.car_list.append(car)
    def move_barrage(self):
        for i in self.car_list:
            i.forward(5)