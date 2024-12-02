import random as r #random 모듈 불러오기

def number_game(): #함수 정의
    print("1부터 10까지의 숫자를 맞춰보세요.") #문자열 출력
    print("이 숫자는 무었일까요?") #문자열 출력
    number = r.randint(1, 10) #randint라는 함수를 이용해서 1~10까지의 정수 중 랜덤으로 하나를 변수에 넣음

    while True: #무한 반복
        number_pre = int(input("예상 숫자 : ")) #사용자가 예상 숫자를 입력하고 그 수를 변수에 저장

        if number_pre == number: #사용자가 예상한 숫자와 랜덤으로 뽑은 수가 같다면 
            print("정답입니다!") #출력
            break #반복문을 나온다
        elif number_pre < number: #사용자가 예상한 숫자가 랜덤으로 뽑은 수보다 작다면
            print("숫자가 작습니다. 다시 입력하세요.") #출력하고 다시 입력하도록 한다.
        else: #사용자가 예상한 숫자가 랜덤으로 뽑은 수보다 크다면
            print("숫자가 큽니다. 다시 입력하세요") #출력하고 다시 입력하도록 한다.

def game_restart(): #게임 재시작 여부 함수 정의
    while True: #break만나기 전까지 무한 반복
        a = input('게임을 다시 하시겠습니까? (y/n): ') #사용자의 입력값 a에 저장
        if a == 'y': #만약에 입력값이 y라면
            number_game() #숫자 게임 함수 실행
        else: #그렇지 않으면
            print('게임 종료') #게임 종료 출력
            break #반복문 끝냄
number_game() #게임 함수 호출
game_restart() #재시작 함수 호출


