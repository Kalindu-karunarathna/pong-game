from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

#create screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


#create left and right paddles
paddle_left = Paddle(-350)
paddle_right = Paddle(350)

left_wall = Turtle()
left_wall.pencolor("white")
left_wall.hideturtle()
left_wall.penup()
left_wall.goto(-340,270)
left_wall.pendown()
left_wall.pensize(20)
left_wall.forward(680)

right_wall = Turtle()
right_wall.pencolor("white")
right_wall.hideturtle()
right_wall.penup()
right_wall.goto(-340,-270)
right_wall.pendown()
right_wall.pensize(20)
right_wall.forward(680)


divider = Turtle()
divider.pencolor("white")
divider.hideturtle()
divider.goto(0,-270)
divider.left(90)
divider.pensize(1)
divider.forward(800)




#make paddles move according to key presses

screen.listen()
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")


ball = Ball()
score=Score()




is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect ball collision with wall
    if ball.ycor()>240 or ball.ycor()<-240:
        ball.bounce_y()

    #detect ball collision with paddles
    if ball.distance(paddle_right)<60 and ball.xcor()>320 or ball.distance(paddle_left)<60 and ball.xcor()<-320:
        ball.bounce_x()




    #detect if ball pass the left and right margins
    if ball.xcor()>430:
        ball.restart()
        score.right_score()
        ball.move_speed = 0.1

    if ball.xcor()<-430:
        ball.restart()
        score.left_score()
        ball.move_speed = 0.1


    if score.l_score==3 or score.r_score==3:
        is_game_on = False
        screen.clear()
        screen.bgcolor("black")
        score.final_score()


screen.exitonclick()


