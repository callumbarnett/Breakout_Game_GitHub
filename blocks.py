from turtle import Turtle


class BlueBlock(Turtle):

    def __init__(self, position):
        super().__init__()
        self.block_destroyed = False
        self.shape('square')
        self.shapesize(stretch_len=9.9, stretch_wid=1.9)
        self.color('blue')
        self.penup()
        self.goto(position, 0)

    def clear_block(self):
        self.hideturtle()
        self.goto(0, 600)
        self.block_destroyed = True

    def next_level(self, position):
        self.block_destroyed = False
        self.goto(position, 0)
        self.showturtle()


class GreenBlock(Turtle):

    def __init__(self, position):
        super().__init__()
        self.block_destroyed = False
        self.shape('square')
        self.shapesize(stretch_len=9.9, stretch_wid=2)
        self.color('green')
        self.penup()
        self.goto(position, 40)

    def clear_block(self):
        self.hideturtle()
        self.goto(0, 600)
        self.block_destroyed = True

    def next_level(self, position):
        self.block_destroyed = False
        self.goto(position, 40)
        self.showturtle()


class YellowBlock(Turtle):

    def __init__(self, position):
        super().__init__()
        self.block_destroyed = False
        self.shape('square')
        self.shapesize(stretch_len=9.9, stretch_wid=2)
        self.color('yellow')
        self.penup()
        self.goto(position, 80)

    def clear_block(self):
        self.hideturtle()
        self.goto(0, 600)
        self.block_destroyed = True

    def next_level(self, position):
        self.block_destroyed = False
        self.goto(position, 80)
        self.showturtle()


class OrangeBlock(Turtle):

    def __init__(self, position):
        super().__init__()
        self.block_destroyed = False
        self.shape('square')
        self.shapesize(stretch_len=9.9, stretch_wid=2)
        self.color('orange')
        self.penup()
        self.goto(position, 120)

    def clear_block(self):
        self.hideturtle()
        self.goto(0, 600)
        self.block_destroyed = True

    def next_level(self, position):
        self.block_destroyed = False
        self.goto(position, 120)
        self.showturtle()


class RedBlock(Turtle):

    def __init__(self, position):
        super().__init__()
        self.block_destroyed = False
        self.shape('square')
        self.shapesize(stretch_len=9.9, stretch_wid=2)
        self.color('red')
        self.penup()
        self.goto(position, 160)

    def clear_block(self):
        self.hideturtle()
        self.goto(0, 600)
        self.block_destroyed = True

    def next_level(self, position):
        self.block_destroyed =False
        self.goto(position, 160)
        self.showturtle()
