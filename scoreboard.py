from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.leftscore=0
        self.rightscore=0
        self.scoring()
    def scoring(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightscore, align="center", font=("Courier", 80, "normal"))

    def lscore(self):
        self.leftscore+=1
        self.scoring()
    def rscore(self):
        self.rightscore+=1
        self.scoring()
