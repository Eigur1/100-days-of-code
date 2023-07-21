from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")

    def draw_scoreboard(self, score):
        self.clear()
        self.goto(0, 350)
        self.pendown()
        self.write(f"Score = {score}", True, font=("Arial", 14), align="center")
