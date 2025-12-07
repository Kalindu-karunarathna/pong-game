from turtle import Turtle

#paddle class use to create paddles
#and go_up, go_down methods make paddles move according to key press
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)

    def go_up(self):
        new_y = self.ycor() + 70
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 70
        self.goto(self.xcor(), new_y)

