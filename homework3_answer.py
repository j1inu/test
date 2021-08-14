# 3차 과제 answer
'''
[homework 3차 주제]
1. 함수
2. 여러가지 Mission
'''

# [함수]
## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 16p참고
'''
# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    """
    # 설정(작성할 부분1)
    # 펜 사이즈, 펜 색상(list)
    rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    t.pensize(pen_size)

    # 그리기(작성할 부분2)
    for i in range(7):
        t.setheading(90)
        t.penup()
        t.setpos(x+(rainbow_size / 2) - i * pen_size, y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.circle(rainbow_size / 2 - i * pen_size, 180)

import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

# 이제 draw_rainbow를 활용하여 무지개를 마음껏 그려보자(작성할 부분3)
draw_rainbow(t, 100, 10, 100, 51)
draw_rainbow(t, 200, 15, 100, -51)
draw_rainbow(t, 200, 15, -100, -51)
draw_rainbow(t, 200, 15, -100, 51)

turtle.mainloop()
'''

# [여러가지 Mission]
# Problem1: factorial 계산하기
# ※ factorial이란?: 1에서 시작하여 "어떤 범위에 있는 모든 정수를 곱하는 것" 
'''
num = int(input("숫자를 입력하세요>> "))

print("결과: 1", end='')
facto = 1
for i in range(2, num+1):
    facto = i * facto
    print(f"*{i}", end='')
print(f'={facto}')
'''

# Problem2: 유클리드 알고리즘으로 최대공약수 구하기(GCD: Greatest Common Divisor)
## [유클리드의 GCD 알고리즘] - while문 사용하기
## 1. 두 수 가운데 큰 수를 x, 작은 수를 y라고 한다.
## 2. y가 0이면 최대 공약수는 x와 같고 알고리즘을 종료한다.
## 3. r <- x % y
## 4. x <- y
## 5. y <- r
'''
x = int(input("첫번째 정수를 입력하세요: "))
y = int(input("두번째 정수를 입력하세요: "))

if x < y:
    x, y = y, x

while (y != 0):
    r = x % y
    x, y = y, r
print(f"최소 공약수는 {x}입니다")
'''


# Problem3: 아스키코드를 활용한 슬롯머신 문제
# ASCII 코드의 33~39번(총 7개)의 특수문자를 활용하여 슬롯머신 만들기
'''
import random

slot = [0, 0, 0]
select = 0

print('[Slot Machine GAME]')
while True:
    select = int(input("1.게임시작 // 2.나가기>>"))
    if select == 1:
        while True:
            print("<SLOT MACHINE>")
            # 코인 넣기
            coin = int(input("코인을 넣어주세요!(1.코인넣기//2.그만하기)>>"))
            if coin == 1:
                # slot에 랜덤한 정수 3개 대입
                for i in range(3):
                    slot[i] = random.randint(33, 39)
                # slot 화면 출력
                print('-------------------')
                print('|  %c  |  %c  |  %c  |' % (chr(slot[0]), chr(slot[1]), chr(slot[2])))
                print('-------------------')
                # 결과출력
                if slot[0] == slot[1] == slot[2]:
                    print('JACK POT!!!!\n')
                else:
                    print('아쉽습니다. 다음 기회에!\n')
            elif coin == 2:
                print('슬롯머신을 중단합니다.\n')
                break
            else:
                print('잘못 입력하셨습니다.\n')
    elif select == 2:
        print("게임을 종료합니다:D\n\n")
        break
    else:
        print("잘못 입력하셨습니다.\n\n")
'''


# Problem4: "달팽이는 올라가고 싶다...!" 문제(for문으로 풀면 안풀리는 문제)
# (참고사이트: https://www.acmicpc.net/problem/2869)
# 시간측정 방법: import time // start = time.time() // print("time: ", time.time()-start)
# [조건]
# 조건1: 입력1>> 2 1 5 [결과: 4] // 입력2>> 5 1 6 [결과: 2] // 입력3>> 2 1 10000000 [결과: 9999901]
# 조건2: 위 조건1의 모든 입력에 대한 수행시간이 1초 이내에 완료
# Hint1: .split(' ')
# Hint2: 필요 하다면, import math // .floor .ceil() 등등 사용하기
## 1. for문으로 작성한 경우
'''
import time

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]

count = 1
while V >= 0:
    V = V - A
    if V <= 0:
        break
    V = V + B
    count += 1
print(count)
print('time: ', time.time()-start)
'''

## 2. 공식을 세워 연산한 경우
'''
import math
import time

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]

result1 = 2 + math.floor((V-A)/(A-B))
result2 = 1 + math.ceil((V-A)/(A-B))
result = 1 + (V-A)/(A-B)

print(result1)
print(result2)
print(result)
print("time: ", time.time()-start)
'''

## 3. 홈페이지에서 채점을 받고 싶다면?
## import sys // A, B, V = map(int, sys.stdin.readline().split())
'''
import math
import sys
import time

A, B, V = map(int, sys.stdin.readline().split())

result = 1 + math.ceil((V-A)/(A-B))

print(result)
print("time: ",  time.time()-start)
'''

