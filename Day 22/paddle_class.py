from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pad_type):
        super().__init__()
        self.create_paddle(pad_type)

    def create_paddle(self, pad_type):
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.speed("fastest")
        cords = ((430, 0), (-430, 0))
        if pad_type == 1:
            self.goto(cords[0])
        else:
            self.goto(cords[1])
        self.setheading(90)

    def move_north(self):
        if self.ycor() < 280:
            if self.heading() != 90:
                self.setheading(90)
            self.forward(15)

    def move_south(self):
        if self.ycor() > -280:
            if self.heading() != 270:
                self.setheading(270)
            self.forward(15)
