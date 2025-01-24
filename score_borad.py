from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_points = 0
        self.r_points = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_points,align="center",font=("courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.r_points, align="center", font=("courier", 80, "normal"))

    def r_score(self):
        self.r_points += 1
        self.update()

    def l_score(self):
        self.l_points += 1
        self.update()








