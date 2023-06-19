from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.tracer(0) ## draws nothing till the update method

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.turtle_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
        
    if snake.turtle_list[0].xcor() > 290 or snake.turtle_list[0].xcor() < -290 or snake.turtle_list[0].ycor() > 290 or snake.turtle_list[0].ycor() < -290:
        is_game_on=False
        score.game_over()

    for turtle in snake.turtle_list[1:]:
        if snake.turtle_list[0].distance(turtle) < 10:
            is_game_on=False
            score.game_over()

my_screen.exitonclick()