from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

#create screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


#create left and right paddles
paddle_left = Paddle(-350)
paddle_right = Paddle(350)




#make paddles move according to key presses
screen.listen()
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")


ball = Ball()



is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect ball collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect ball collision with paddles
    if ball.distance(paddle_right)<60 and ball.xcor()>320 or ball.distance(paddle_left)<60 and ball.xcor()<-320:
        ball.bounce_x()

    #detect if ball pass the left and right margins
    if ball.xcor()>400 or ball.xcor()<-400:
        ball.restart()


screen.exitonclick()


