from turtle import Turtle
import random as rd


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1)
        self.setheading(rd.randint(0, 360))
        self.setheading(240)

    def reset_ball(self):
        self.home()
        # self.setheading(rd.randint(0, 360))
        self.setheading(189)

    def bounce_borders(self):
        if 280 < self.ycor() < 300:
            if 0 < self.heading() < 90:
                self.setheading(360-self.heading())
            if 90 < self.heading() < 180:
                self.setheading(180-self.heading()+180)
            self.forward(5)
        if -300 < self.ycor() < -280:
            if 180 < self.heading() < 270:
                self.setheading(270 - self.heading() + 90)
            if 270 < self.heading() < 359:
                self.setheading(360 - self.heading())
            self.forward(5)

    def bounce_paddle(self):
        if 270 < self.heading() < 360:
            self.setheading(360 - self.heading() + 180)
        elif 0 < self.heading() < 90:
            self.setheading(90 - self.heading() + 90)
        elif 90 < self.heading() < 180:
            self.setheading(180 - self.heading())
        elif 180 < self.heading() < 270:
            self.setheading(270 - self.heading() + 270)
        self.forward(20)
