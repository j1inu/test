# 4차 개인 교습 answer
'''
[4th_lesson 범위]
1. 반복문 연습문제
2. 함수
3. 튜플
4. 딕셔너리
'''

# [반복문 Mission 추가]
## 반복문 mission4: turtle을 활용하여 무지개 그리기 (이후 함수에도 연개할 예정이므로 반드시 수행)
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
'''
import turtle

# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
rainbow_size = 500         # 무지개 크기(너비)
pen_size = 30              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(10)                # 거북이 속도 설정 

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)
for i in range(7):
    t.setheading(90)
    t.penup()
    t.setpos(rainbow_size/2 - i*pen_size, 0)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size/2 - i*pen_size, 180)

win.mainloop()
'''

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
# DrawStar_100 함수 정의해주기
def DrawStar_100():
    """
    한 변의 길이가 100인 별모양을 그리는 함수.
    """
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)

win = turtle.Screen()
DrawStar_100()
win.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
# DrawStar() 함수 정의해주기
def DrawStar(length):
    """한 변의 길이 length를 입력받고, 그 변의 길이를 가진 별을 그리는 함수"""
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.left(72)

win = turtle.Screen()
DrawStar(250)
win.mainloop()
'''
## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
# getRandomNum() 함수 정의해주기
def getRandomNum():
    """1~100 사이의 랜덤 정수를 반환하는 함수"""
    return random.randint(1,100)

num = getRandomNum()
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
# add 함수 정의해주기 
def add(x, y):

    return x+y, x-y
num = add(1,2)
print(num, type(num))

X, Y = add(100, 60)
print(X, Y)
'''


# [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 =              # ()로 튜플 만들기
numbers2 =              # ()없이 튜플 만들기
print(numbers1, type(numbers1))
print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
## ※ 결과를 비교해보는 것이 중요!!
'''
num1 =          # ()로 만든 경우
num2 =          # (,)로 만든 경우
num3 =          # 숫자 1개만 넣어준 경우
num4 =          # 숫자, 로 만들어준 경우
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = (100, 110, 10)
numbers = list(numbers)     # 튜플을 list로 변환하기
print(numbers, type(numbers))
numbers = tuple(numbers)
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
## ※ 결과를 확인하는 것이 중요!!
'''
# 패킹
a = 
b = 
              # numbers로 a,b를 패킹해주기 
print("numbers:", numbers, type(numbers))   # 결과확인(데이터 값, 자료형 확인)

# 언패킹
c, d = numbers      # numbers에 포함된 숫자를 c, d로 언패킹해주기 
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')        # 결과확인(데이터 값, 자료형 확인)

# 응용: a, b의 값 바꿔주기
print("a: ", a)
print("b: ", b)
a, b = b, a         
print("a: ", a)     # 결과 확인
print("b: ", b)
'''

## 연습문제5: 튜플과 관련된 함수
## ※ 결과 확인이 중요!!
'''
numbers = 100, 546, 896, 10, 777
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(777))   # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print(numbers.index(246))   # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''

