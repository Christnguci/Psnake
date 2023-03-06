from turtle import Turtle
ALIGNMENT="center"
FONT =("Courier",20,"normal")



class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        with open('data.txt','r') as data :
            self.highscore=int(data.read())
        data.close()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score: {self.score}, High score: {self.highscore}",align =ALIGNMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align =ALIGNMENT,font =FONT)

    def reset(self):
        if self.score> self.highscore:
            self.highscore=self.score
            with open('data.txt',"w") as data:
                data.write(str(self.highscore))
            data.close()
        self.score=0
        self.update_scoreboard()
        
