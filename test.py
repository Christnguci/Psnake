from turtle import Turtle, Screen


screen=Screen()
screen.setup(600,600)
screen.title("My snake")
#screen.tracer(n)-screen is update after n movements of turtle
#screen.tracer(n,delay(m))-n movements of turtle and delay m milisecond 
screen.tracer(0)
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in starting_positions:
    new_segment =Turtle("square")
    new_segment.color("black")
    new_segment.goto(position)
    segments.append(new_segment)

#movement
def up():
    segments[0].setheading(90)
def left():
    segments[0].setheading(180)
def down():
    segments[0].setheading(270)
def right():
    segments[0].setheading(0)
def clear():
    segments.reset() 
import time
keep_forward=True

while keep_forward:
    screen.update()
    time.sleep(0.07)
    for seg_num in range(len(segments)-1,0,-1):
         new_x=segments[seg_num-1].xcor()
         new_y=segments[seg_num-1].ycor()
         segments[seg_num].goto(new_x,new_y)
         segments[seg_num].clear()
    
    segments[0].forward(10)
    segments[0].clear()
    

        
    screen.listen()
    screen.onkey(key="w",fun=up)
    screen.onkey(key="a",fun=left)
    screen.onkey(key="d",fun=right)
    screen.onkey(key="s",fun=down)



        
   




    


    
screen.onkey(key="c",fun=clear)
screen.exitonclick()