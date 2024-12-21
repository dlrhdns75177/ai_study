class Person: #Person 클래스 생성
    def __init__(self, name, gender, age): #매직메서드 사용해서 내부 초기 변수 선언
        self.name = name #이름
        self.gender = gender #성별
        self.age = age #나이
    def display(self): #클래스 내부에 정보 보여주는 함수 선언
        while self.gender != 'female' and self.gender != 'male': #성별 female 과 male이 아니라면 무한반복
            print('성별을 female 혹은 male로 다시 입력해주세요.') #출력문
            input_info = input('이름, 성별, 나이를 입력해주세요.').split(' ') #사용자 정보 다시 입력 받기
            self.name = input_info[0] #input_info는 지역변수이기 때문에 새롭게 업데이트를 해야함
            self.gender = input_info[1]
            self.age = int(input_info[2])
        print(f"이름: {self.name}, 성별: {self.gender}") #이름과 성별 같은 줄에 출력
        print(f"나이: {self.age}") #나이 다음 줄에 출력
    def greet(self): #클래스 내부에 인사 멘트 함수 선언
        if self.age < 10: #나이가 10살보다 적으면 
            print(f"안녕하세요, {self.name}! 어린이이시군요") #출력문
        elif self.age < 20: #나이가 20살보다 적으면 
            print(f"안녕하세요, {self.name}! 청소년이시군요") #출력문
        else: #나이가 20살 포함 그 이상이면
            print(f"안녕하세요, {self.name}! 성인이시군요") #출력문

input_info = input('이름, 성별, 나이를 입력해주세요.').split(' ') #사용자 정보 입력
input_info[2] = int(input_info[2]) #나이는 정수로 바꾸기

info_display = Person(input_info[0], input_info[1], input_info[2]) #Person의 객체 선언
info_display.display() #display 함수 호출
info_display.greet() #greet 함수 호출

