from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move(self, direction):
        new_y = self.ycor() + direction * 20
        self.goto(self.xcor(), new_y)

    def go_up(self):
        self.move(1)

    def go_down(self):
        self.move(-1)
