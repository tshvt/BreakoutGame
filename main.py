from turtle import Screen
from paddle import Paddle
from blocks import YellowBlock, GreenBlock, OrangeBlock, RedBlock
from ball import Ball
from scoreboard import Score, Life
import time

screen = Screen()
screen.setup(width=800, height=1000)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

coords_yellow_blocks = [(-350, 50), (-260, 50), (-170, 50), (-80, 50), (10, 50), (100, 50), (190, 50), (280, 50),
                        (370, 50),
                        (-370, 100), (-280, 100), (-190, 100), (-100, 100), (-10, 100), (80, 100), (170, 100), (260, 100),
                        (350, 100)]

coords_green_blocks = [(x, y + 100) for (x, y) in coords_yellow_blocks]

coords_orange_blocks = [(x, y + 100) for (x, y) in coords_green_blocks]

# coords_red_blocks = [(x, y + 90) for (x, y) in coords_orange_blocks]

lives_coords = [(-370, 350), (-320, 350), (-270, 350)]


yellow_blocks = [YellowBlock(coords) for coords in coords_yellow_blocks]
green_blocks = [GreenBlock(coords) for coords in coords_green_blocks]
orange_blocks = [OrangeBlock(coords) for coords in coords_orange_blocks]
# red_blocks = [RedBlock(coords) for coords in coords_red_blocks]
lives = [Life(coords) for coords in lives_coords]
score = Score()
paddle = Paddle()
ball = Ball()
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if paddle.xcor() >= 330:
        screen.onkey(paddle.stop_moving_forward, "d")
    if paddle.xcor() <= -330:
        screen.onkey(paddle.stop_moving_backward, "a")
    else:
        screen.onkey(paddle.move_left, "a")
        screen.onkey(paddle.move_right, "d")

    if ball.ycor() <= -300 and ball.distance(paddle) <= 50:
        ball.bounce_y()
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce_x()
    if ball.ycor() >= 390:
        ball.bounce_y()
    if ball.ycor() <= -400:
        lives[-1].hideturtle()
        lives.remove(lives[-1])
        ball.reset_ball()
        if not lives:
            game_is_on = False
            score.lose()

    for block in yellow_blocks:
        if ball.distance(block) <= 35:
            ball.bounce_y()

            block.hideturtle()
            yellow_blocks.remove(block)
            score.add_points("yellow")
    for block in green_blocks:
        if ball.distance(block) <= 35:
            ball.bounce_y()
            block.hideturtle()
            green_blocks.remove(block)
            score.add_points("green")
    for block in orange_blocks:
        if ball.distance(block) <= 35:
            ball.bounce_y()
            ball.increase_speed()
            block.hideturtle()
            orange_blocks.remove(block)
            score.add_points("orange")
    if not yellow_blocks and not green_blocks and not orange_blocks:
        game_is_on = False
        score.win()


screen.exitonclick()
