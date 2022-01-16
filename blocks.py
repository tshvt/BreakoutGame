from turtle import Turtle


class YellowBlock(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.color("yellow")
        self.goto(coords)


class GreenBlock(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.color("green")
        self.goto(coords)


class OrangeBlock(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.color("orange")
        self.goto(coords)


class RedBlock(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color("red")
        self.goto(coords)



