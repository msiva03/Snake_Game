from turtle import Turtle, Screen
import time
from snake import Snake
from turtledemo.penrose import start

screen = Screen()

screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()





screen.exitonclick()