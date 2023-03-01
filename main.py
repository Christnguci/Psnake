from turtle import Turtle,Screen,colormode
import time
from snake import Snake
from food import Food
import math
colormode(255)

screen=Screen()
screen.setup(600,600)
screen.title("My snake")
screen.bgcolor("black")
snake=Snake()
food=Food()

screen.listen()
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="a",fun=snake.left)
screen.onkey(key="d",fun=snake.right)
screen.onkey(key="s",fun=snake.down)
screen.tracer(0) 

def distance():
    x= int(math.sqrt((snake.x_head()-food.x_food())*(snake.x_head()-food.x_food())+(snake.y_head()-food.y_food())*(snake.y_head()-food.y_food())))
    return x
eat_times=0
Score=Turtle()
Score.color("white")
keep_forward=True
while keep_forward:
    screen.update()
    time.sleep(0.07)
    snake.move()  
    if distance()<15:
        food.move()
        snake.add()
        eat_times+=1
        Update_score()
        if eat_times%5==0:
            food.shapesize(2)
        else:
            food.shapesize(1)
#Updatescore
    def Update_score ():
        Score.clear()
        Score.penup()
        Score.goto(200, 200)
        Score.pendown()
        font = ("Arial", 10,"normal")
        Score.write(f"Your score: {eat_times}",font=font)
        Score.hideturtle()


screen.exitonclick()
#hello