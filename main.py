from turtle import Turtle,Screen,colormode
import time,math
from snake import Snake
from food import Food
import tkinter as tk
from tkinter import messagebox
from scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.title("My snake")
screen.bgcolor("black")
#Updatescore
def wall_detect(snake):
    x=int(math.sqrt((snake.head.xcor()*snake.head.xcor())))
    y=int(math.sqrt((snake.head.ycor()*snake.head.ycor()))) 
    if x>305 or y >305 :
        return True
    return False

snake=Snake()
food=Food()
score_board=Scoreboard()
user_answer=messagebox.askyesno("Alert"," Do you want to play the game ? ")
while user_answer:
        screen.listen()
        screen.onkey(key="w",fun=snake.up)
        screen.onkey(key="a",fun=snake.left)
        screen.onkey(key="d",fun=snake.right)
        screen.onkey(key="s",fun=snake.down)
        screen.tracer(0)
        keep_forward=True
        while keep_forward:
                dead_tail=False
                screen.update()
                time.sleep(0.1)
                snake.move()  
                if snake.distance(food)<20:
                    food.move()
                    snake.add()
                    score_board.score+=1
                    score_board.update_scoreboard()
                    if score_board.score%5==0:
                        food.shapesize(2)
                    else:
                        food.shapesize(1)
                for segment in snake.segments:
                    if segment==snake.head:
                        pass
                    elif  snake.distance(segment) < 5:
                            dead_tail=True
                if wall_detect(snake) or dead_tail:
                            # Create a Tkinter root window
                            root = tk.Tk()
                            # Hide the root window
                            root.withdraw()
                            # Show a pop-up message box with a message and an OK button
                            messagebox.showinfo("Score",f"Your final score is {score_board.score}, High score {score_board.highscore}.")
                            score_board.reset()
                            # Destroy the root window
                            root.destroy()
                            keep_forward=False
                            
        break
            
                    

#hello