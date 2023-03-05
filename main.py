from turtle import Turtle,Screen,colormode
import time,math
from snake import Snake
from food import Food
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

def deadth_wall(snake):
    x=int(math.sqrt((snake.head.xcor()*snake.head.xcor())))
    y=int(math.sqrt((snake.head.ycor()*snake.head.ycor())))
    if x>305 or y >305 :
        return True
    return False


un_deadth=True
def Play_game():
    gameover=False
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
            time.sleep(0.1)
            snake.move()  
            if snake.distance(food)<15:
                food.move()
                snake.add()
                eat_times+=1
                Update_score(eat_times)
                if eat_times%5==0:
                    food.shapesize(2)
                else:
                    food.shapesize(1)
            for segment in snake.segments:
                if segment==snake.head:
                      pass
                elif  snake.distance(segment) < 5:
                        gameover=True
            if deadth_wall(snake) or gameover:
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
        user_answer=messagebox.askyesno("Continue ?"," Do you want to play the game ? ")
        if user_answer:
            screen.listen()
            Play_game()
        else:
            break


#hello