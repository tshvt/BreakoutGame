from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.goto(340, 320)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def add_points(self, color):
        if color == "yellow":
            self.score += 1
        elif color == "green":
            self.score += 3
        elif color == "orange":
            self.score += 5
        self.clear()
        self.update_score()

    def lose(self):
        self.goto(0, -50)
        self.write(f"You lose! Score: {self.score}", align=ALIGNMENT, font=FONT)

    def win(self):
        self.goto(0, -50)
        self.write(f"You win! Score: {self.score}", align=ALIGNMENT, font=FONT)


class Life(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.goto(coords)
        self.shapesize(stretch_len=2, stretch_wid=2)



