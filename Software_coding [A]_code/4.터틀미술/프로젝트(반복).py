import turtle as t

t.speed(0) # 터틀의 속도를 가장 빠르게 설정
t.shape('turtle')
t.bgcolor('black') # 배경색을 검은색으로 설정
colors = ['orange', 'skyblue', 'yellow']

i = 0
while True:
    t.color(colors[i % 3]) # i를 3으로 나눈 나머지에 해당하는 색상을 선택하여 터틀 색상 설정
    t.fd(i) # 터틀이 앞으로 i만큼 이동 (반복이 진행될수록 이동 거리가 커짐)
    t.lt(119) # 터틀이 왼쪽으로 119도 회전 (정삼각형에서 조금 벗어난 각도로 회전)
    i += 1