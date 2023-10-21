from paddle import Paddle
from turtle import *


sc=Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.tracer(0)
sc.screensize(canvheight=400,canvwidth=400)


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_is_on=True

while game_is_on:
    sc.update()


sc.exitonclick()
