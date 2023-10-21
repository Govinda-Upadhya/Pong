from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.shapesize(stretch_wid=1,stretch_len=1)
    self.penup()
    self.x_move=10
    self.y_move=10
  def move(self):
    x_cor=self.xmove +10
    y_cor=self.ymove+10
    self.goto(x_cor,y_cor)
  def bouncex(self):
    self.xmove*=-1
  def bouncey(self):
    self.ymove*=-1
  def positons(self):
    y_core = self.ycor() + 20
    return y_core
  def miss(self):
    self.goto(0,0)
