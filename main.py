from turtle import Turtle,Screen,colormode
import time
from snake import Snake
from food import Food
import math
import tkinter as tk
from tkinter import messagebox
screen=Screen()
screen.setup(600,600)
screen.title("My snake")
screen.bgcolor("black")
def create_a_snake ():
    snake=Snake()
    return snake
def create_food():
    food=Food()
    return food
#Updatescore
Score=Turtle()
Score.color("white")
def Update_score (eat_times):
    Score.clear()
    Score.penup()
    Score.goto(200, 200)
    Score.pendown()
    font = ("Arial", 10,"normal")
    Score.write(f"Your score: {eat_times}",font=font)
    Score.hideturtle()
def distance(snake,food):
    x= int(math.sqrt((snake.x_head()-food.x_food())*(snake.x_head()-food.x_food())+(snake.y_head()-food.y_food())*(snake.y_head()-food.y_food())))
    return x


def deadth(snake):
    x=int(math.sqrt((snake.x_head()*snake.x_head())))
    y=int(math.sqrt((snake.y_head()*snake.y_head())))
    if x>305 or y >305 :
        return True
    return False
un_deadth=True

def Play_game():
    snake=create_a_snake()
    food=create_food()
    eat_times=0
    screen.onkey(key="w",fun=snake.up)
    screen.onkey(key="a",fun=snake.left)
    screen.onkey(key="d",fun=snake.right)
    screen.onkey(key="s",fun=snake.down)
    screen.tracer(0)
    keep_forward=True
    while keep_forward:
            screen.update()
            time.sleep(0.07)
            snake.move()  
            if distance(snake,food)<15:
                food.move()
                snake.add()
                eat_times+=1
                Update_score(eat_times)
                if eat_times%5==0:
                    food.shapesize(2)
                else:
                    food.shapesize(1)
            if deadth(snake):
                        # Create a Tkinter root window
                        root = tk.Tk()

                        # Hide the root window
                        root.withdraw()

                        # Show a pop-up message box with a message and an OK button
                        messagebox.showinfo("Score",f"Your final score is {eat_times}.")

                        # Destroy the root window
                        root.destroy()
                        Turtle.reset()
                        break
            
                    

while un_deadth:
        user_answer=messagebox.askokcancel("Continue ?"," Do you want to play the game ? ")
        if user_answer:
            screen.listen()
            Play_game()
        else:
            break


#hello