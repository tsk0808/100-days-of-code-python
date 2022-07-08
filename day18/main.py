import turtle as t
import random


t.Turtle()

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

random_color = (random.choice(color_list))

#   펜의 색상을 바꾸는 명령어이다.
#    다른 옵션이 있는지는 다 확인해 보지 않아서 모르지만, 기본은 1.0이고 255(RGB)로 바꿀 수 있다.
t.colormode(255)

#   그림판에 펜을 뗀다는 의미이다. 즉, 그림판 위에서 공중으로 펜이 올라간다는 의미로 penup.
t.penup()

t.speed("fastest")
t.hideturtle()


def left_up():

    '''
    방향바꾸기
    거북이 머리 돌리기

    거북이가 원하는 방향으로 가기 위해서는 먼저 머리를 돌려야 겠죠? 만약 오른쪽으로 가는데 머리는 왼쪽을 보고 있다면 정~말 어색할 뿐 아니라 충돌의 위험도 있겠지요?^^

    거북이 머리 돌리기는 이전에 다루었던 lt(), rt() 함수로 왼쪽, 오른쪽으로 돌릴 수도 있지만 이 seth() 함수를 사용하면 360도 중 원하는 각도로 머리 방향을 바꿀 수 있어서 편리합니다.

    seth, setheading()

    둘 다 가능하면 당연히 단순한 seth()를 사용하는 것이 좋겠지요? 중요한 사실은 기본 방향인 동쪽이 0 이라는 것입니다. 그러면 북쪽은 90이 되겠지요?

    동 - seth(0)

    북 - seth(90)

    서 - seth(180)

    남 - seth(270)


    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    '''

def right_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)


for _ in range(5):
    for _ in range(10):

        #   turtle.dot은 터틀 펜이 위치한 곳이 그리는 원의 중심이 되는 점에서 turtle.circle과 차이가 있습니다. 그리고, 원의 내부도 색으로 채우게 되는 점에서도 크게 다릅니다. 아래 코드를 실행해보면 차이를 알아볼 수 있습니다. 
        t.dot(20, (random.choice(color_list)))
        t.setheading(180)
        t.forward(50)
    left_up()
    for _ in range(10):
        t.forward(50)
        t.dot(20, (random.choice(color_list)))
    right_up()


screen = t.Screen()
screen.exitonclick()
