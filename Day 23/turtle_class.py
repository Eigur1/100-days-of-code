from turtle import Turtle

class Turtle_Cross(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def move(self):
        self.forward(5)
    def at_end(self):
        if self.ycor() > 280:
            return True
    def reser_turtle(self):
        self.goto(0,-280)