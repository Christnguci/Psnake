from turtle import Turtle,Screen,colormode
import random
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
class Food(Turtle) :

    def __init__(self):
          super().__init__()
          self.shape("circle")
          self.color(r,g,b)
          self.pensize(1)
          self.penup()
          self.move()

    def x_food(self):
         x= int(self.xcor())
         return x
    def y_food(self):
         y= int(self.ycor())
         return y
     
    def move(self):
         new_x=random.randint(-280,280)
         new_y=random.randint(-280,280)
         self.penup()
         self.goto(new_x,new_y)
         
     


