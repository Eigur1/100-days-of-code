from turtle import Turtle, Screen


def draw_shapes():
    coñito = Turtle()
    coñito.speed(10)
    for i in range(3, 100):
        angel = 360 / i
        initial = coñito.pos()
        initial= [round(initial[0]), round(initial[1])]
        coñito.forward(100)
        pos_final =[]
        while pos_final != initial:
        #while coñito.distance(initial) > 0.1:
        #for e in range (1,i):
            coñito.right(angel)
            coñito.forward(100)
            print((coñito.pos()*-1))
            pos_final = [round(coñito.pos()[0]), round(coñito.pos()[1])]
        coñito.right(angel)

draw_shapes()
screen = Screen()
screen.exitonclick()
