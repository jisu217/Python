import turtle as t
import random

t.speed(0)
t.shape('turtle')
t.bgcolor('black')
colors = ['deeppink', 'orange', 'gold', 'greenyellow', 'deepskyblue', 'magenta']

for i in range(300):
    t.penup() # 터틀의 펜을 올려 이동할 때 선이 그려지지 않도록 함

    # randint는 random 모듈의 함수, random.randint(a, b): 두 값 사이의 임의의 정수를 반환
    x = random.randint(-400, 400) # -400에서 400 사이의 랜덤한 x 좌표 생성
    y = random.randint(-400, 400) # -400에서 400 사이의 랜덤한 y 좌표 생성
    t.goto(x, y) # 랜덤하게 생성된 (x, y) 좌표로 터틀 이동

    c = random.choice(colors) # random.choice(seq): 시퀀스(seq)에서 임의의 요소 하나를 반환.
    t.color(c)

    t.pendown() # 터틀의 펜을 내려서 그리기 시작
    draw = random.choice([t.circle, t.dot]) # 원 그리기(t.circle) 또는 점 찍기(t.dot) 중 하나 무작위로 선택
    size = random.randint(1, 100) # 1에서 100 사이의 랜덤 크기 값 설정
    draw(size) # 선택된 도형을 설정된 크기로 그리기