from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        with open("High_score.txt", "r") as dc:
            self.high_score = dc.read()
            dc.close()
        print(self.high_score)

    def draw_scoreboard(self, score):
        self.clear()
        self.goto(0, 350)
        self.pendown()
        self.write(f"Score = {score}. High score = {self.high_score}", False, font=("Arial", 14, "normal"), align="center")
        self.penup()

    def game_over_he(self, local_score):
        if int(local_score) > int(self.high_score):
            self.high_score = local_score
            with open("High_score.txt", "w") as dc:
                dc.write(str(local_score))

                dc.close()
        self.clear()
