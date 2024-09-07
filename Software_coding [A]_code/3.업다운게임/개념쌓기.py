while True: # 무한 반복이 필요할 떄_ 사용자가 q를 입력할 떄까지 계속해서 숫자를 입력받음    answer = input('숫자를 입력하세요. 종료는 q를 입력하세요.')
    answer = input('숫자를 입력하세요. 종료는 q를 입력하세요.')
    if answer == 'q':
        print('프로그램을 종료합니다.')
        break
    elif int(answer)%2 == 1:
        print('홀수!')
    else:
        print('짝수!')
