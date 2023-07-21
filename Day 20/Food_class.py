from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):

        self.ht()
        new_cords = (rd.randint(-280,280), rd.randint(-280,280))
        self.goto(new_cords)
        self.st()
