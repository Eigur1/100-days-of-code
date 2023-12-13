from turtle import Turtle, Screen

cumito = Turtle()
screen = Screen()


def move_forward():
    cumito.forward(15)


def move_backwards():
    cumito.backward(15)


def tilt_clockwise():
    cumito.right(5)


def tilt_counter_clockwise():
    cumito.left(5)


def clear():
    cumito.clear()
    cumito.penup()
    cumito.home()
    cumito.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(tilt_clockwise, "d")
screen.onkey(tilt_counter_clockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()
sketch()
