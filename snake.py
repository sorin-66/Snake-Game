from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.boa = []
        self.create_snake()
        self.head = self.boa[0]
        self.length = len(self.boa) - 1

    def snake_reset(self):
        tail = self.boa[3:]
        for segment in tail:
            print(segment)
            segment.reset()
        self.boa = self.boa[:3]
        print(self.boa)
        for i in range(3):
            print(self.boa[i].color())
            print(START_POSITION[i])
            self.boa[i].goto(START_POSITION[i])
            self.boa[i].setheading(0)
            print(self.boa[i].position())
        print(len(self.boa))
        self.length = 2

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("green")
        snake.goto(position)
        self.boa.append(snake)

    def extend_snake(self):
        last_position = self.boa[-1].position()
        self.add_segment(last_position)
        self.length = len(self.boa) - 1

    def move(self):
        for i in range(self.length, 0, -1):
            #print(self.length)
            next_poz = self.boa[i - 1].position()
            self.boa[i].goto(next_poz)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
