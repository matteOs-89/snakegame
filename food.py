import random
from turtle import Turtle, Screen


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-200, 280)
        random_y = random.randint(-200, 280)
        self.goto(random_x, random_y)

