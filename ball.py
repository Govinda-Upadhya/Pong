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
    
