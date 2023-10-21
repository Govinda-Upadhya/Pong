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

while True:
    sc.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()< -280 :
        ball.bouncey()
    if ball.distance(pad1)<55 and ball.xcor()>340 or ball.distance(pad2)<55 and ball.xcor()>-340:
        ball.bouncex()
    if ball.xcor()>500 :
        ball.miss()
        scoreborad.rscore()
        ball.bouncex()
    if ball.xcor() < -500:
        ball.miss()
        scoreborad.lscore()
        ball.bouncex()



sc.exitonclick()
