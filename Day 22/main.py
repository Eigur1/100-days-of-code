from turtle import Screen
from scoreboard_class import Scoreboard
from paddle_class import Paddle
from field_class import Field
from ball_class import Ball
import time

screen = Screen()
screen.screensize(canvwidth=900, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)

field = Field()

pad1 = Paddle(1)
pad2 = Paddle(2)


screen.onkeypress(pad1.move_north, "Up")
screen.onkeypress(pad1.move_south, "Down")
screen.onkeypress(pad2.move_north, "w")
screen.onkeypress(pad2.move_south, "s")
screen.listen()

ball = Ball()

scoreboard = Scoreboard()

screen.update()
is_game_on = True
score1 = 0
score2 = 0
while is_game_on:
    ball.bounce_borders()
    if (ball.distance(pad1) < 50 and ball.xcor() < 410) or (ball.distance(pad2) < 50 and ball.xcor() > -410):
        print(ball.heading())
        ball.bounce_paddle()
        print(ball.heading())
        screen.update()
    if ball.xcor() > 450:
        score1 += 1
        ball.reset_ball()
        screen.update()
    if ball.xcor() < -450:
        score2 += 1
        ball.reset_ball()
        screen.update()
    ball.forward(1)
    scoreboard.draw_score([score1, score2])
    screen.update()
    time.sleep(0.001)

screen.exitonclick()
