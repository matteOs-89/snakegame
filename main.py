from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Os Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # check to confirm if snake is in  physical contact with food
    if snake.direction.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # place game parameters and boundaries

    if snake.direction.xcor() > 290 or snake.direction.xcor() < -290 or snake.direction.ycor() > 300 or snake.direction.ycor() < -290:
        game_on = False
        score.game_over()

    # detect if snake is in contact with its own tail.

    for seg in snake.turtle_bunch[1:]:
         if snake.direction.distance(seg) < 10:
            game_on = False
            score.game_over()









screen.exitonclick()