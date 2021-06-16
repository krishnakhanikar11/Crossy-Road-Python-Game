from turtle import Turtle

class Our(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -270)
        self.move()
        self.res()

    def move(self):
        self.forward(20)

    def res(self):
        self.goto(0, -270)
