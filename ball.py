from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    #make ball move
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    #make ball bounce and increase the speed after bounce
    def bounce_y(self):
        self.y_move*=-1
        self.move_speed*=0.9

    #make ball bounce
    def bounce_x(self):
        self.x_move*=-1

    #when restarted, make ball in the center and change the move direction
    def restart(self):
        self.goto(0,0)
        self.x_move*=-1
        self.move_speed *= 0.9

