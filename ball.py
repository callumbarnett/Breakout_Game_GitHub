from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('grey')
        self.penup()
        self.goto(0, -330)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def side_bounce(self):
        self.x_move *= -1

    def top_bounce(self):
        self.y_move *= -1

    def reset_ball(self, position):
        self.hideturtle()
        self.goto(position, -330)
        self.showturtle()
        self.top_bounce()
        self.move()

    def paddle_contact(self):
        self.y_move *= -1
