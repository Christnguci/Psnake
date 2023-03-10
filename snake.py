from turtle import Turtle,colormode
import random,math

starting_positions=[(0,0),(-20,0),(-40,0)]
UP= 90
DOWN=270
LEFT=180
RIGHT=0
MOVE=10
colormode(255)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)


#create initial snake
class Snake(Turtle) :

    def __init__(self):
          super().__init__()
          self.segments= []
          self.create_snake()
          self.head=self.segments[0]
    def create_snake(self):
         for position in starting_positions:
            new_segment =Turtle("square")
            new_segment.color(r,g,b)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    #if snake catch food
    def add(self):
            new_segment =Turtle("square")
            new_segment.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            new_segment.penup()
            self.segments.append(new_segment)
    def distance(self,object):
        x= int(math.sqrt((self.head.xcor()-object.xcor())*(self.head.xcor()-object.xcor())+(self.head.ycor()-object.ycor())*(self.head.ycor()-object.ycor())))
        return x

#movement
  
    def up(self):
         if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading()!= UP:
             self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_num-1].xcor()
                new_y=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE)

    