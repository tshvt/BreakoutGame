from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=8)
        self.color("grey")
        self.goto(0, -320)

    def move_left(self):
        self.backward(50)

    def move_right(self):
        self.forward(50)

    def stop_moving_forward(self):
        self.forward(0)

    def stop_moving_backward(self):
        self.backward(0)


