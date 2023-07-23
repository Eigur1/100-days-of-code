from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()

    def draw_score(self, score_list):
        cords = ((-80, 240), (80, 240))
        self.clear()
        for i in range(0, 2):
            self.goto(cords[i])
            self.pendown()
            self.write(f"{score_list[i]}", font=("Arial", 60, "normal"), align="center")
            self.up()
        self.penup()
