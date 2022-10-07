
from turtle import Turtle

TURTLE_START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtle_bunch = []
        self.create_snake()
        self.direction = self.turtle_bunch[0]

    def create_snake(self):
        for i in TURTLE_START_POSITION:
            self.add_segment(i)


    def add_segment(self, i):
        t_obj = Turtle(shape="square")
        t_obj.color("white")
        t_obj.penup()
        t_obj.goto(i)
        self.turtle_bunch.append(t_obj)

    def extend(self):
        self.add_segment(self.turtle_bunch[-1].position())

    def move(self):
        for t_num in range(len(self.turtle_bunch) - 1, 0, -1):
            new_x = self.turtle_bunch[t_num - 1].xcor()
            new_y = self.turtle_bunch[t_num - 1].ycor()
            self.turtle_bunch[t_num].goto(new_x, new_y)
        self.direction.forward(MOVE_STEPS)

    def up(self):
        if self.direction.heading() != DOWN:
            self.direction.setheading(UP)

    def down(self):
        if self.direction.heading() != UP:
            self.direction.setheading(DOWN)

    def left(self):
        if self.direction.heading() != RIGHT:
            self.direction.setheading(LEFT)

    def right(self):
        if self.direction.heading() != LEFT:
            self.direction.setheading(RIGHT)




