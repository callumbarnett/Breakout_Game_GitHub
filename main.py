from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import BlueBlock, GreenBlock, YellowBlock, OrangeBlock, RedBlock
from scoreboard import Title, Score, Lives
import time

game_on = True
ball_speed = 0.05

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=900)
screen.title('Breakout')
screen.tracer(0)

title = Title()
score = Score()
lives = Lives()

paddle = Paddle()
paddle_length = 150
ball = Ball()

starting_position = -500

blue_block_1 = BlueBlock(-500)
blue_block_2 = BlueBlock(-300)
blue_block_3 = BlueBlock(-100)
blue_block_4 = BlueBlock(100)
blue_block_5 = BlueBlock(300)
blue_block_6 = BlueBlock(500)

green_block_1 = GreenBlock(-500)
green_block_2 = GreenBlock(-300)
green_block_3 = GreenBlock(-100)
green_block_4 = GreenBlock(100)
green_block_5 = GreenBlock(300)
green_block_6 = GreenBlock(500)

yellow_block_1 = YellowBlock(-500)
yellow_block_2 = YellowBlock(-300)
yellow_block_3 = YellowBlock(-100)
yellow_block_4 = YellowBlock(100)
yellow_block_5 = YellowBlock(300)
yellow_block_6 = YellowBlock(500)

orange_block_1 = OrangeBlock(-500)
orange_block_2 = OrangeBlock(-300)
orange_block_3 = OrangeBlock(-100)
orange_block_4 = OrangeBlock(100)
orange_block_5 = OrangeBlock(300)
orange_block_6 = OrangeBlock(500)

red_block_1 = RedBlock(-500)
red_block_2 = RedBlock(-300)
red_block_3 = RedBlock(-100)
red_block_4 = RedBlock(100)
red_block_5 = RedBlock(300)
red_block_6 = RedBlock(500)

all_blue_blocks = [blue_block_1, blue_block_2, blue_block_3, blue_block_4, blue_block_5, blue_block_6]
all_green_blocks = [green_block_1, green_block_2, green_block_3, green_block_4, green_block_5, green_block_6]
all_yellow_blocks = [yellow_block_1, yellow_block_2, yellow_block_3, yellow_block_4, yellow_block_5, yellow_block_6]
all_orange_blocks = [orange_block_1, orange_block_2, orange_block_3, orange_block_4, orange_block_5, orange_block_6]
all_red_blocks = [red_block_1, red_block_2, red_block_3, red_block_4, red_block_5, red_block_6]

all_blocks = [blue_block_1, blue_block_2, blue_block_3, blue_block_4, blue_block_5, blue_block_6,
              green_block_1, green_block_2, green_block_3, green_block_4, green_block_5, green_block_6,
              yellow_block_1, yellow_block_2, yellow_block_3, yellow_block_4, yellow_block_5, yellow_block_6,
              orange_block_1, orange_block_2, orange_block_3, orange_block_4, orange_block_5, orange_block_6,
              red_block_1, red_block_2, red_block_3, red_block_4, red_block_5, red_block_6]


screen.listen()
screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() < -580 or ball.xcor() > 580:
        ball.side_bounce()

    # Detect collision with top of screen
    if ball.ycor() > 430:
        ball.top_bounce()

    # Detect ball leaving screen
    if ball.ycor() < -450:
        lives.life_lost()
        ball.reset_ball(paddle.xcor())

    # Contact with paddle
    if ball.ycor() < -320 and ball.distance(paddle) < paddle_length:
        ball.paddle_contact()

    # Lives
    if lives.lives == 0:
        lives.game_over()
        score.game_over_score()
        game_on = False

    # Collision with blue blocks
    if ball.ycor() == -30 or ball.ycor() == 30:
        if ball.distance(blue_block_1) < 100:
            blue_block_1.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(blue_block_2) < 100:
            blue_block_2.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(blue_block_3) < 100:
            blue_block_3.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(blue_block_4) < 100:
            blue_block_4.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(blue_block_5) < 100:
            blue_block_5.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(blue_block_6) < 100:
            blue_block_6.clear_block()
            ball.top_bounce()
            score.point()

    # Collision with green blocks
    if ball.ycor() == 10 or ball.ycor() == 70:

        if ball.distance(green_block_1) < 100:
            green_block_1.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(green_block_2) < 100:
            green_block_2.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(green_block_3) < 100:
            green_block_3.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(green_block_4) < 100:
            green_block_4.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(green_block_5) < 100:
            green_block_5.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(green_block_6) < 100:
            green_block_6.clear_block()
            ball.top_bounce()
            score.point()

    # Collision with yellow block
    if ball.ycor() == 50 or ball.ycor() == 110:

        if ball.distance(yellow_block_1) < 100:
            yellow_block_1.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(yellow_block_2) < 100:
            yellow_block_2.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(yellow_block_3) < 100:
            yellow_block_3.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(yellow_block_4) < 100:
            yellow_block_4.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(yellow_block_5) < 100:
            yellow_block_5.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(yellow_block_6) < 100:
            yellow_block_6.clear_block()
            ball.top_bounce()
            score.point()

    # Collision with orange blocks
    if ball.ycor() == 90 or ball.ycor() == 150:

        if ball.distance(orange_block_1) < 100:
            orange_block_1.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(orange_block_2) < 100:
            orange_block_2.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(orange_block_3) < 100:
            orange_block_3.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(orange_block_4) < 100:
            orange_block_4.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(orange_block_5) < 100:
            orange_block_5.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(orange_block_6) < 100:
            orange_block_6.clear_block()
            ball.top_bounce()
            score.point()

    # Collision with red blocks
    if ball.ycor() == 130 or ball.ycor() == 190:

        if ball.distance(red_block_1) < 100:
            red_block_1.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(red_block_2) < 100:
            red_block_2.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(red_block_3) < 100:
            red_block_3.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(red_block_4) < 100:
            red_block_4.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(red_block_5) < 100:
            red_block_5.clear_block()
            ball.top_bounce()
            score.point()

        if ball.distance(red_block_6) < 100:
            red_block_6.clear_block()
            ball.top_bounce()
            score.point()

    # Level up
    if blue_block_1.block_destroyed and blue_block_2.block_destroyed and blue_block_3.block_destroyed and blue_block_4 \
            and blue_block_5.block_destroyed and blue_block_6.block_destroyed and green_block_1.block_destroyed\
            and green_block_2.block_destroyed and green_block_3.block_destroyed and green_block_4.block_destroyed\
            and green_block_5.block_destroyed and green_block_6.block_destroyed and yellow_block_1.block_destroyed\
            and yellow_block_2.block_destroyed and yellow_block_3.block_destroyed and yellow_block_4.block_destroyed \
            and yellow_block_5.block_destroyed and yellow_block_6.block_destroyed and orange_block_1.block_destroyed \
            and orange_block_2.block_destroyed and orange_block_3.block_destroyed and orange_block_4.block_destroyed \
            and orange_block_5.block_destroyed and orange_block_6.block_destroyed and red_block_1.block_destroyed \
            and red_block_2.block_destroyed and red_block_3.block_destroyed and red_block_4.block_destroyed \
            and red_block_5.block_destroyed and red_block_6.block_destroyed:

        score.score += 3
        if paddle.level > 5:
            paddle_length -= 50
            paddle.level_up()

        if paddle.level == 5:
            ball_speed -= 0.01

        for blue_block in all_blue_blocks:

            blue_block.next_level(starting_position)
            starting_position += 200

        starting_position = -500

        for green_block in all_green_blocks:

            green_block.next_level(starting_position)
            starting_position += 200

        starting_position = -500

        for yellow_block in all_yellow_blocks:

            yellow_block.next_level(starting_position)
            starting_position += 200

        starting_position = -500

        for orange_block in all_orange_blocks:
            orange_block.next_level(starting_position)
            starting_position += 200

        starting_position = -500

        for red_block in all_red_blocks:
            red_block.next_level(starting_position)
            starting_position += 200

        starting_position = -500

        ball.reset_ball(paddle.xcor())
        time.sleep(1)


screen.mainloop()
