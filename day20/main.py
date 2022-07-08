from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)

#   Set Background Color
screen.bgcolor("black")

#   Set Title
screen.title("Snake Game")

#   turtle 모듈의 tracer 함수는 스크린창의 출력을 조절 할 수 있는 함수입니다. (*구체적인 내용은 아래의 표를 참고)
'''
tracer = 0 tracer = 1 코드 0 코드 0코드 1코드 1 코드 2코드 2 코드 0,1,2
한번에
출력가능 코드 0,1,2
하나씩
출력

'''
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()
