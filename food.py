from random import randint
from turtle import Turtle, Screen


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.register_shape("apple.gif")
        self.screen.addshape("apple.gif")
        self.shape("apple.gif")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-270, 270), y=randint(-270, 270))

    def draw_border(self):
        self.goto(x=-300, y=-300)
        self.pendown()
        self.pensize(20)
        for i in range(4):
            self.setheading(90 - 90 * i)
            self.forward(600)
        self.penup()
        self.refresh()
