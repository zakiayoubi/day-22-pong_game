from turtle import Turtle
PADDLE1_POSITION = (350, 0)
PADDLE2_POSITION = (-350, 0)


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


