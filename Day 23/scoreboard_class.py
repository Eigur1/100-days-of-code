from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.hideturtle()
        self.penup()

    def draw_score(self, score):
        cords = (-150, 290)
        self.clear()
        self.goto(cords)
        self.pendown()
        self.write(f"Score: {score}", font=("Arial", 20, "normal"), align="center")
        self.up()

