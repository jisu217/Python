# 파이썬에서 그래픽적으로 그림을 그리기 위한 도구 중 하나인 turtle 모듈
  # turtle 모듈에서는 기본적으로 turtle, classic, triangle, square, arrow, turtle, circle 등의 모양을 지원

# import turtle as t

# 터틀의 모양을 '거북이'로 설정
# t.shape('turtle')

# 터틀이 현재 방향으로 100만큼 앞으로 이동
# t.fd(100)  # fd는 forward의 약자

# 터틀이 오른쪽으로 90도 회전
# t.rt(90)  # rt는 right turn의 약자

# 터틀이 새로운 방향(오른쪽으로 90도 회전한 방향)으로 100만큼 앞으로 이동
# t.fd(100)

# 터틀이 왼쪽으로 60도 회전
# t.lt(60)  # lt는 left turn의 약자

# t.fd(100)


# 터틀에게 반복 명령어 내리기
import turtle as t
t.shape('turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue']

# 리스트에 있는 각 색상마다 반복하여 터틀의 움직임을 명령
for c in colors:
    t.color(c) # 터틀의 색상을 현재 반복에서의 색상으로 변경
    t.fd(200)
    t.lt(144)