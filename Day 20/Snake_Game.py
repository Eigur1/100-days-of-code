from turtle import Turtle, Screen
import random as rd
import time
from Snake_class import Snake
from Food_class import Food
from Score_board import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)
cord_list = [(0, 0), (-20, 0), (-40, 0)]
segment_list = []

snake = Snake()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.listen()

food = Food()
scoreboard = Scoreboard()


def collision_with_food():
    if snake.segment_list[0].distance(food) < 17:
        return True


local_score = 0

while True:
    snake.move()
    snake.check_collision_wall()
    if collision_with_food():
        food.generate_food()
        snake.snake_extend()
        local_score += 1
    scoreboard.draw_scoreboard(local_score)
    if not snake.detect_tail_collision():
        scoreboard.game_over_he(local_score)
        snake.snake_reset()
        local_score = 0 
    screen.update()

