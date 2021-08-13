# 2차 개인 교습 mission
'''
[수업내용]
1. 문자열 입출력 함수(input(), print())
2. 자료형과 변수 그리고 주석
3. 연산1(산술, 문자열, 복합할당)
4. 연산2(비교, 논리, 멤버십)
5. 입출력과 자료형 변환
6. 조건문
'''

# [문자열 입출력 함수]
## 문자열 입출력 함수 Mission
'''
name = input("이름을 입력하세요>> ")
print(f"{name}님 안녕하세요")
'''
# [자료형과 변수]
## [자료형]
## -숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
'''
print(3, 49, 38, 9)
print(type(9))      #int
'''
## - 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
'''
print(12.12, 312.41, 3.14, 1.414)
print(type(312.41))     #float
'''
## -문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기
'''
print("집가고싶다")
print('지 가야지')
print(type("집가고싶다"))        #string
'''
## mission2>> 문자열로 인용구호('') 출력하기
'''
print('김첨지는 "왜 성렁탕을 사왔는데 왜 먹지를 못하니"라고 말했다.')
print("사자가'으르렁'소리를 내었다.")
'''
## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정
'''
print('가나','다라', sep='@@')
print('마바사')
print('안녕하세요', end='뿅')
print('반갑습니다')
'''
## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
'''
print(True)
print(False)
print(type(True))       #bool
'''

## [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터
## mission>> 라인하르트(or 내 게임 주 캐릭터)의 이름, 공격력, 공격속도, 최대거리(reach)를
## 변수로 저장하고 출력해보자.
## 라인하르트 정보: https://namu.wiki/w/%EB%9D%BC%EC%9D%B8%ED%95%98%EB%A5%B4%ED%8A%B8(%EC%98%A4%EB%B2%84%EC%9B%8C%EC%B9%98)#s-4.2
'''
name = '드라군'
attack = 100
speed = 10
reach = 12
print('Character Spec: ',name, attack, speed, reach)
print(f"나의 이름은 {name}이다")
'''

# [연산]
## [연산(1)]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자
'''
# 변수 생성 후, 할당연산자로 값 넣어보기 
'''
## 숫자산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기
'''
print(7+3)
print(7-3)
print(7*3)
print(7/3) 
print(7//3) 
print(7%3) 
print(7**3)
'''
## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어
## 출력해보자
'''
tag1 = '오늘부터1일'
tag2 = '#너내꺼하자'
tag = tag1 + tag2
print(tag)
'''
## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자

string = '안녕하세요'
print(string*10)

## 복합할당연산자: 연산계의 줄임말
## mission>> 복함할당연산자를 활용하여 위에서 언급한 내 주 캐릭터의 스펙을 바꿔보자!
'''
attack = 100
attack += 10        # attack = attack+10
print(attack)
attack -= 10        # attack = attack-10
print(attack)
attack *= 10        # attack = attack*10
print(attack)
attack /= 10        # attack = attack/10
print(attack)
'''

# [연산(2)]
## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 출력하여 정답확인하기
'''
print(5>8)      
print(3<8)     
print(10>=7)   
print(200>=751) 
print(5==11)  
print(5!=5)
print("포항항항하항항" == "포항항항하항항")
print("illililillllllilil" != "illililillllllilil")
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10)     
print("정신나갈거같아" == "점심나가서먹을거같아" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야?") 
print(not 5==5)
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print("a" in "abc") 
print("d" in "abc") 
print("기" not in "신서유기")
'''

# [입출력과 자료형 변환]
## mission1>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
'''
x = input("x를 입력해주세요>>")
y = input("y>>")

result = x + y
print(result)
'''

## mission2>> mission1에서 제대로 된 값이 나오도록 코드를 수정해보자.
'''
x = int(input("x를 입력해주세요>>"))
y = int(input("y>>"))

result = x + y
print(result)
'''
# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행
## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자
'''
subscriber = int(input("구독자 수를 입력하세요>>>"))
if subscriber >= 1000:
    print("수입창출 가능 대상자입니다")
else:
    print("X")
'''
## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자

money = int(input("보유금액을 입력하세요>>>"))
if money>=20000:
    print("오늘 저녁은 치킨이닭!")
elif money>=10000:
    print("이제는 고오급 음식인 떡볶이 ㅎㅎ")
elif money>=2000:
    print("그래도 굶지는 않는 편의점 삼각김밥!")
else:
    print('없다고 못먹는건 아니다. 친구에세 "한입만!"을 외쳐보자')

