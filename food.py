from turtle import Turtle,Screen
import random
class Food(Turtle) :
    def __init__(self):
          super().__init__()
          self.color("white")
          self.shape("circle")
          self.penup()
          self.move()

    def x_food(self):
         x= int(self.xcor())
         return x
    def y_food(self):
         y= int(self.ycor())
         return y
         
    def move(self):
         new_x=random.randint(-300,300)
         new_y=random.randint(-300,300)
         self.penup()
         self.goto(new_x,new_y)
     


