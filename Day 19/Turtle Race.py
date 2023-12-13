from turtle import Turtle, Screen
import random as rn


def race(screen):
    screen.screensize(canvheight=700, canvwidth=500)
    color_list = ["green", "blue", "yellow", "red", "orange"]
    rn.shuffle(color_list)
    name_list = ["pollita", "culito", "chochito", "tetitas", "escroto"]
    dic = {}
    position = [-225, 250]
    for i in range(0, len(name_list)):
        local_color = color_list[i]
        # local_turtle = Turtle()
        dic[name_list[i]] = Turtle()
        dic[name_list[i]].color(local_color)
        dic[name_list[i]].shape("turtle")
        dic[name_list[i]].penup()
        dic[name_list[i]].goto(position[0], position[1])
        dic[name_list[i]].pendown()
        position[1] -= 100
    draw_exit_line()
    plyr_choice = screen.textinput("Pick your turtle", "Which turtle are you rooting for?")
    a = True
    while a:
        for i in range(0, len(name_list)):
            fw = rn.randint(1, 10)
            dic[name_list[i]].forward(fw)
            if dic[name_list[i]].color()[0] == "orange":
                fw = rn.randint(2, 10)
                dic[name_list[i]].forward(fw)
            if not_at_finish(dic[name_list[i]]):
                a = False
                name = name_list[i]
                winner = dic[name_list[i]]
    if plyr_choice == winner.color()[0]:
        print("You where right, cunt!")
    else:
        print("Wrong, fuckhead!")
    print(f"The winner is {name} as {winner.color()[0]}")

    screen.exitonclick()


def not_at_finish(turtle):
    if turtle.pos()[0] < 200:
        return
    else:
        a = False
        return True


def draw_exit_line():
    esclavo = Turtle()
    esclavo.penup()
    esclavo.goto(200, -350)
    esclavo.pendown()
    esclavo.goto(200, 350)


screen = Screen()
race(screen)
