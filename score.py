from turtle import Turtle

with open(file="data.txt", mode="r") as data:
    highscore = int(data.read())

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore = highscore
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.hideturtle()
        self.score=0
        self.write(f"Score : {self.score} High Score : {self.highscore}", align='center' , font=('Arial',16,'bold') )
    
    def update_score(self):
        self.score+=1
        self.clear()
        if self.highscore < self.score:
            self.write(f"Score : {self.score} High Score : {self.score}", align='center' , font=('Arial',16,'bold') )
        else:
            self.write(f"Score : {self.score} High Score : {self.highscore}", align='center' , font=('Arial',16,'bold') )
    
    def game_over(self):
        if self.highscore < self.score:
            self.highscore=self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
            self.clear()
            self.write(f"Congratz! Final Score is the High Score : {self.highscore}" , align="center", font=("Arial", 16, "bold"))
        self.score = 0
        self.goto(0,0)
        self.write("GAME OVER", align='center' , font=('Arial',20,'normal') )