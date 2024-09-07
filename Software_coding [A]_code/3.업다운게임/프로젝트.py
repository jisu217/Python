import random # 랜덤 숫자를 생성하기 위한 모듈

number = random.randint(1, 100) # 1부터 100 사이의 랜덤 정수를 선택
count = 0 # 사용자가 시도한 횟수를 저장하는 변수

while True:
    # 사용자에게 숫자를 입력받고, 이를 정수로 변환
    answer = int(input('내가 고른 숫자를 맞혀 봐!'))
    count += 1

    # 사용자가 입력한 숫자가 정답일 경우
    if answer == number:
        print('제법이군! 정답이야!')
        print(str(count)+'번 만에 정답을 맞혔어!')
        break

    # 사용자가 입력한 숫자가 정답보다 작은 경우
    elif answer < number:
        print('업 Up!')

    # 사용자가 입력한 숫자가 정답보다 큰 경우
    else:
        print('다운 Down!')
