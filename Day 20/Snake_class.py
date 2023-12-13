from turtle import Turtle, Screen
import random as rd
import time

START_LIST = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()

    def create_snake(self):
        for i in START_LIST:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.segment_list.append(new_segment)

    def move(self):
        nextpos = self.segment_list[0].pos()
        self.segment_list[0].forward(MOVE_DISTANCE)
        for seg in range(1, len(self.segment_list)):
            currentp = self.segment_list[seg].pos()
            self.segment_list[seg].goto(nextpos)
            nextpos = currentp[:]

        time.sleep(0.05)

    def right(self):
        if self.segment_list[0].heading() == 180:
            return
        self.segment_list[0].setheading(0)

    def left(self):
        if self.segment_list[0].heading() == 0:
            return
        self.segment_list[0].setheading(180)

    def up(self):
        if self.segment_list[0].heading() == 270:
            return
        self.segment_list[0].setheading(90)

    def down(self):
        if self.segment_list[0].heading() == 90:
            return
        self.segment_list[0].setheading(270)

    def check_collision_wall(self):
        pos = self.segment_list[0].pos()
        if pos[0] >= 300:
            return self.segment_list[0].goto((-300), pos[1])
        if pos[0] <= -300:
            return self.segment_list[0].goto((300), pos[1])
        if pos[1] >= 300:
            return self.segment_list[0].goto(pos[0], -300)
        if pos[1] <= -300:
            return self.segment_list[0].goto(pos[0], 300)

    def detect_tail_collision(self):
        pos_list = []
        for i in self.segment_list[1:]:
            if self.segment_list[0].distance(i) < 5:
                return False
        return True

    def snake_extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.segment_list.append(new_segment)

    def snake_reset(self):
        for i in self.segment_list:
            i.goto(1000,1000)
        self.segment_list.clear()
        self.create_snake()