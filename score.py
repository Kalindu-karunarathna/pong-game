from turtle import Turtle


#this class use to track and display score
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    #clear the current score and display the updated score
    def update_score(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 280)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    #update left player score
    def left_score(self):
        self.r_score+=1
        self.update_score()

    #update right player score
    def right_score(self):
        self.l_score+=1
        self.update_score()

    #display final scores and the winner
    def final_score(self):
        self.goto(0,0)
        self.write(f"left score = {self.l_score}\nright score = {self.r_score}\n\n" , align="center", font=("Courier", 40, "normal"))
        if self.l_score == 3:
            self.write("🎉left player won🎉" , align="center", font=("Courier", 40, "normal"))
        else:
            self.write("🎉right player won🎉" , align="center", font=("Courier", 40, "normal"))


