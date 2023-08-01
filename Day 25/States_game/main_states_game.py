from turtle import Turtle, Screen
import pandas as pd

state_data = pd.read_csv("50_states.csv")

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.screensize(canvwidth=491, canvheight=725)

turtle = Turtle()
turtle.penup()
turtle.hideturtle()

states_list = state_data["state"].tolist()

game_status = True
guessed_list = []

while game_status:
    input = screen.textinput("Yank game", "Chose ypur state: ")
    if input in states_list:
        xcord = state_data.at[state_data.index[state_data["state"] == input].tolist()[0],"x"]
        ycord = state_data.at[state_data.index[state_data["state"] == input].tolist()[0],"y"]
        turtle.goto(xcord, ycord)
        turtle.write(input, True, align="center", font=["Arial", 8, "normal"])
        guessed_list.append(input)
        states_list.remove(input)

    elif input == "exit":
        game_status = False
    elif input in guessed_list:
        print("Are your retarded by change?")
    else:
        print("That state doesnt exist, whore.")

finaldfug = pd.DataFrame(states_list, columns=["Unguessed states"])
finaldfg = pd.DataFrame(guessed_list, columns=["Guessed states"])
finaldfg.to_csv("Guess_report.csv")
finaldfug.to_csv("Missing_states.csv")

