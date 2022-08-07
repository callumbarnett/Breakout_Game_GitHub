from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 15
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=self.level)
        self.resizemode('user')
        self.color('white')
        self.penup()
        self.goto(0, -350)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.level -= 5
        self.clear()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=self.level)
        self.resizemode('user')
        self.color('white')
        self.penup()
        self.goto(self.xcor(), self.ycor())
