from turtle import Turtle,Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)


# def go_up():
#     new_y = paddle.ycor()+40
#     paddle.goto(350,new_y)
#
# def go_down():
#     new_y = paddle.ycor()-40
#     paddle.goto(350,new_y)

paddle_left = Paddle(-350)
paddle_right = Paddle(350)





screen.listen()
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")



is_game_on = True

while is_game_on:
    screen.update()



screen.exitonclick()


