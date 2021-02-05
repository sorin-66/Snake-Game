from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initializing the screen where the game will be played
screen = Screen()
screen.setup(width=635, height=635, startx=200, starty=0)
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("light blue")
screen.title("Snake Game")
screen.tracer(0)
user_start = screen.textinput(title="Snake Game", prompt='Controls: use arrows or w,s,a,d for '
                                                         'up,down,left,right. Type ok to start')

# game start after the user type ok in the pop-up window
game_is_on = False
ask_user = False
if user_start:
    game_is_on = True

while not ask_user:
    # initializing the game parts
    snake = Snake()
    food = Food()
    food.draw_border()

    # activate the keys to control the snake
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="d", fun=snake.right)
    screen.update()
    scoreboard = Scoreboard()
    X_MARGIN = 290
    Y_MARGIN = 290
    delay = 0.5
    while game_is_on:
        screen.update()
        time.sleep(delay)
        snake.move()
        if scoreboard.score < 10:
            delay = 0.25
        elif scoreboard.score < 20:
            delay = 0.2
        elif scoreboard.score < 30:
            delay = 0.1
        elif scoreboard.score < 40:
            delay = 0.05
        else:
            delay = 0.01

        # detect snake collision with food
        if snake.head.distance(food) < 15:
            food.shape("apple.gif")
            food.refresh()
            scoreboard.update_score()
            snake.extend_snake()

        # detect collision with wall
        if snake.head.xcor() > X_MARGIN or snake.head.xcor() < -X_MARGIN \
                or snake.head.ycor() > Y_MARGIN or snake.head.ycor() < -Y_MARGIN:
            game_is_on = False
            scoreboard.game_over()

        # detect collision with tail
        snake_tail = snake.boa[3:]
        for snake_body in snake_tail:
            if snake.head.distance(snake_body) < 15:
                game_is_on = False
                scoreboard.game_over()

    # ask user if want to play again
    if not ask_user:
        ask_user = True

        user_restart = screen.textinput(title="Snake Game",
                                        prompt='Do you want to play again?. Type ok to start or no to exit')
        if user_restart == "ok":
            screen.clear()
            screen.bgcolor("light blue")
            game_is_on = True
            screen.tracer(0)
            ask_user = False
        elif user_restart == "no":
            ask_user = True


screen.exitonclick()
