from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-220,220)
        self.level = 1
        self.increaseLevel()

    def increaseLevel(self):
        self.write(f"Level: {self.level}", align='center' , font=("Courier" , 25, 'normal'))

    def finalLevel(self):
        self.goto(0, 0)
        self.write(f"GAME OVER !! Level: {self.level}", align='center', font=("Courier", 25, 'normal'))

    def updateLevel(self):
        self.level += 1
        self.clear()
        self.increaseLevel()
