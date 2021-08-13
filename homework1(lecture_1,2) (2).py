# 1차 과제 
'''
[과제범위]
1. 문자열 입출력 함수(input(), print())
2. 연산1(산술, 문자열, 복합할당)
3. 연산2(비교, 논리, 멤버십)
4. 입출력과 자료형 변환
5. 조건문
'''

# [문자열 입출력 함수 homework]
## 문자열 입출력 함수 Mission2(ppt 7p 참고)


# [연산(1) homework]
## 숫자산술연산 Mission
## : 아래 수식들의 결과를 각 줄에 주석으로 작성하기 
'''
print(264+8748)     #
print(7-150)        #
print(15*7)         #
print(100/13)       #
print(100//13)      #
print(100%13)       #
print(21**3)        #
'''

## 문자열연산 homework1
## : 문자열 덧셈을 활용하여 2개의 문자열을 덧셈한 결과를 출력해보자
print(138+234)
print(684+2878)
## 문자열연산 homework2
## : 문자열 곱셈을 활용하여 같은 문장이 10회 반복되는 문장을 출력해보자
string = 'Hello'
print(string*10)

## 복합할당연산자 homework
## : 아래 복합할당연산자를 풀어쓴 의미와 식의 답을 그 줄의 주석으로 작성해보자.
## (계산 결과는 프로그램 실행을 통해 확인 후 작성해도 상관 없음.)
'''
number = 10     # 10
number += 15    # 25
number *= 3     # 30
number /= 7     # 1.4285714285714286
number -= 100   # -90
'''

# [연산(2) homework]
## 비교연산 homework
## : 아래 비교연산의 결과 예상하여 주석으로 작성해보고 연산결과와 비교해보자
'''
print(15>7)             #True
print(163<199)          #True
print(1>=2)             #False
print(7660>=7660)       #True
print(5==5)             #True
print(700!=700)         #False
print("ijijjjjjijjiiiiji" == "ijijjjjjjijjiiiiji")      #False
print("illililillllllilil" != "illililillllllilil")     #False
'''

## 논리연산 homework
## : 아래 논리연산의 결과 예상하여 주석으로 작성해보고 연산결과와 비교해보자
'''
print(75 <100 and 37 >= 40)     #    False   
print("따-따-따-따, 따따다 따따따!" == "따-따-따-따- 물보라를 일으켜~" or "크크루크크" == "크크루삥뽕")     #  False or True 
print(not 5813==8446)           #    True
'''

## 멤버십연산 homework
## : 아래 멤버십연산의 결과 예상하여 주석으로 작성해보고 연산결과와 비교해보자
'''
print("a" in "angry")      # True
print("b" not in "bird")   # False
'''

# [입출력과 자료형 변환 homework]
## 입출력과 자료형 변환 Mission3(자료2 ppt 32p 참고)
## : 출생년도를 입력하고 나이를 출력해보자.
'''
age = int(input("출생년도를 입력하세요 >>"))
result = 2021-age+1
print(result)
'''

# [조건문 homework]
## 조건문 Mission3(자료2 ppt 41p)
## : 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 평균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자

'''
literature = int(input("국어 점수를 입력하세요 >> "))
english = int(input("영어 점수를 입력하세요 >> "))
math = int(input("수학 점수를 입력하세요 >> "))
result = literature + english + math
if result > 180:
    print("보충 대상자가 아닙니다. 즐거운 방학보내세요")
else:
    print("보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ")
'''

## 조건문 Mission4(자료2 ppt 43p)
## : Up-down 게임 만들기
## random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기

import random

print("[Up-Down Game]")
random_num = random.randint(1, 100)
while True:
    # 사용자가 숫자를 입력
    # random_num과 비교하여 '정답/Up/Down'을 출력하는 코드 작성
    # 아래 코드에 내용 추가하기 

    your_num = int(input("숫자입력>>>"))
    if your_num == random_num:
        print("정답입니다~~!")
        break
    elif your_num > random_num:
        print("Down")
    else:
        print("Up")













