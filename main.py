from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
import math
screen=Screen()
screen.setup(600,600)
screen.title("My snake")
screen.bgcolor('black')
#screen.tracer(n)-screen is update after n movements of turtle
#screen.tracer(n,delay(m))-n movements of turtle and delay m milisecond 
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
keep_forward=True
eat_times=0
while keep_forward:
    screen.update()
    time.sleep(0.07)
    snake.move()    
    if distance() <15:
        food.move()
        snake.add()
        eat_times+=1
        if eat_times%5==0:
            food.shapesize(5)
        else:
            food.shapesize(1)
            

    

screen.exitonclick()
