# homework 2차(3rd_lesson Mission)
'''
[homework 2차 주제]
1. 리스트
2-1. 반복문 for
2-2. 반복문 while
'''


# [리스트]
## 리스트 mission1(3차 ppt 45p 참고)
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))

import turtle
from typing import List

color = ['red', 'green', 'blue']    # Hint: 리스트 객체인 color의 원소 순서에 집중할 것!
win = turtle.Screen(1)
t = turtle.Turtle('turtle')     #거북이 객체
t.pensize(30)

# 빨강색
t.pencolor(0)            # 작성부분1: (0)안 채우기
t.forward(200)

# 초록색
t.penup(0)
t.setpos(0, 30)
t.pencolor(color[0])            # 작성부분2: (1)안 채우기
t.pendown(1)
t.forward(200)

# 파란색
t.penup(1)
t.setpos(0, 60)
t.pencolor(2)            # 작성부분3: (2)안 채우기
t.pendown(2)
t.forward(200)

turtle.mainloop(200)


## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다
'''
pull_up = [3, 16, 2, 5, 10, 7]

## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
pull_up.append(9)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
pull_up[1] = '20'
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
temp = pull_up[2:]
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬
pull_up.sort()
'''

## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기
'''
num = int(input("출력할 구구단의 단 수>>"))
for x in range(1,10):
    print("%d * %d = %d" %(num, x, num*x))
'''

## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기
'''
for x in range(2,10):
    for y in range(1,10):
        print("%d * %d = %d" %(x,y,x*y))
'''
## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자
'''
num = int(input("출력할 구구단의 단 수>>"))
x = 1
while x<10:
    print("%d * %d = %d" %(num, x, num*x))
    x += 1
'''
## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.


## 반복문 mission3: 영단어 타자연습 프로그램
# -영타연습 Program-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.
'''
words = ['James Edward Harden', 'Kyrie Andrew Irving', 'point Guard', 'I love NBA']

# 영단어 연습 기능 구현


# 결과 출력(전체 단어 개수, 맞춘 단어 개수, 틀린 단어 개수 출력)

'''
words = ['James Edward Harden', 'Kyrie Andrew Irving', 'point Guard', 'I love NBA']

score = 0
for word in words:
    print(word)
    data = input()
    if word == data:
        score += 1

print("전체 문제 개수:", len(words))
print("맞힌 문제 개수:", score)
print("틀린 문제 개수:", len(words)-score)
