import time
from turtle import Screen
from paddle import Paddle
from ball import  Ball
from score_borad import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)
score_points = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.rest_position()
        score_points.l_score()


    if ball.xcor() < -380:
        ball.rest_position()
        score_points.r_score()


screen.exitonclick()
