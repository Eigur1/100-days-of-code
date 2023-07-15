from turtle import Turtle, Screen


def dotted_line(reps):
    pollita = Turtle()
    for i in range(0,reps):
        pollita.forward(10)
        pollita.penup()
        pollita.forward(10)
        pollita.pendown()


dotted_line(20)

screen = Screen()
screen.exitonclick()
