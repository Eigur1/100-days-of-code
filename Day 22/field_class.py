from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.draw_field()

    def draw_field(self):
        self.goto(0, 350)
        self.setheading(270)
        while self.ycor() > -310:
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()
        self.penup()
