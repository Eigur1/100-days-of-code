from turtle import Turtle, Screen

screen = Screen()


car = Turtle()
car.penup()
car.shape("square")
car.shapesize(stretch_len=2)
car.setheading(180)

screen.exitonclick()