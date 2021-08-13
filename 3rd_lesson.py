# 3차 개인 교습 lesson
'''
[3차 개인 교습 범위]
1. 리스트(list)
2-1. for 반복문
2-2. while 반복문
'''

# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## 연습문제>> 자신이 좋아하는 NBA 선수들 5명으로 올스타 팀을 만들어보자.
'''
BK_player = ["카이리 어빙", "브래들리 빌", "케빈 듀란트", "야니스 아데토쿤보", "조엘 엠비드"]
print(BK_player)

## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 선수 명단에 후보선수 1명을 추가해보자.
BK_player.append("르브론 제임스")

print(BK_player)


## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 선수명단에 내가 가장 좋아하는 선수만을 출력해보자
print(BK_player[2])

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 리스트의 선수 중 1명의 선수를 다른 선수로 변경해보자
BK_player[4] = '제임스 하든'
print(BK_player)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 이 선수들 중 시합 시작 시, 벤치에 앉을 선수 1명을 리스트에서 삭제해보자
del BK_player[1]
print(BK_player)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번째, 2번째~끝, 3번째~4번째에 위치한 선수들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.

print(BK_player[:3])
BK_player[2], BK_player[3] = BK_player[3], BK_player[2]
print(BK_player)

## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자
print(len(BK_player))

## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 선수들의 이름을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자
BK_player.sort()
print(BK_player)
BK_player.sort(reverse=True)
print(BK_player)
'''

# [반복문]
## 반복문이란?: 반복적인 작업을 컴퓨터에 시키기 위한 명령.
## 종류: for문(횟수, 시퀀스 자료형), while문(조건)
## 시퀀스 자료형이란?: "순서"가 있는 자료형 (리스트, 문자열, range객체, 튜블, 딕셔너리)

## range() 함수 연습문제: range()를 활용하여
# 여러 활용 해보기 & list로 만들어 결과 확인하기
'''
print(list(range(10)))
print(list(range(3,11)))
print(list(range(3,15,2)))
print(list(range(50,0,-1)))
'''
## [for 반복문]
## : "횟수 or 시퀀스 자료"에 대한 반복문
## [문법] for 변수 in 시퀀스자료:
##           반복할 문장
## for문 연습문제1: range()를 활용한 "횟수" 반복. 원하는 문자열을 10번 반복해서 출력해보자.
'''
for i in range(10):
    print("안녕")
'''
## for문 연습문제2: list를 활용하여 for 반복문 실행시켜 보기
'''
BK_player = ["카이리 어빙", "브래들리 빌", "케빈 듀란트", "야니스 아데토쿤보", "조엘 엠비드"]
for player in BK_player:
    print(player + " 화이팅!")
'''
## for문 연습문제3: 문자열을 활용하여 for 반복문 실행시켜보기
'''
for a in "안녕하세요":
    print(a)
'''
## 이중 for문 연습문제: 이중 for문을 활용하여 높이5의 직각삼각형 만들기
'''
for x in range(1,6):
    for y in range(x):
        print("*", end='')
    print("")
'''
## [while 반복문]
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용
'''
x = 0
while x<10:
    print("안녕하세요")
    x += 1
'''
## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자
'''
while True :
    select = int(input("프로그램에서 나가려면 -1을 입력하세요>>>"))
    if select == -1:
        break
'''
## while문 + continue 연습문제
## : continue 문을 활용하여 1~10까지 숫자 중 홀수만 출력하는 프로그램 작성
'''
i = 0
while i<10:
    i += 1
    if i % 2 == 0:
        continue
    print("%d" %i )
'''




