from turtle import Turtle


class Title(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 350)
        self.pencolor('white')
        self.write('BREAKOUT', align='center', font=('Courier', 50, 'normal'))


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-500, 350)
        self.pencolor('white')
        self.write(self.score, align='center', font=('Courier', 50, 'normal'))

    def point(self):
        self.score += 10
        self.clear()
        self.write(self.score, align='center', font=('Courier', 50, 'normal'))

    def game_over_score(self):
        self.goto(0, -250)
        self.write(f"Score: {self.score}", align='center', font=('Courier', 50, 'normal'))


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.hideturtle()
        self.goto(450, 350)
        self.pencolor('white')
        self.write(f"Lives: {self.lives}", align='center', font=('Courier', 30, 'normal'))

    def life_lost(self):
        self.lives -= 1
        self.clear()
        self.goto(450, 350)
        self.pencolor('white')
        self.write(f"Lives: {self.lives}", align='center', font=('Courier', 30, 'normal'))

    def game_over(self):
        self.goto(0, -200)
        self.write('GAME OVER', align='center', font=('Courier', 80, 'normal'))


