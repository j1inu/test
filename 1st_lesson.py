# 1차 교습 mission
'''
[수업 내용]
1. python 개발 환경 구축(Anaconda, Pycharm, Git&Github 설치 및 가입)
2. 설치한 프로그램들의 연동(가상환경-Pycharm, Pycharm-Github)
3. 간단한 코드 작성 후 Github에 Commit & Push 수행
'''

# Mission1. 감격스러운 나의 첫 코드: Hello_world
'''
print("Hello World!!")
'''
# Mission2. python과 친해지기
## Mission2-1: 정사각형 그리기
'''
import turtle

win=turtle.Screen()
t = turtle.Turtle('turtle')

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

win.mainloop()
'''

## Mission2-2: 정삼각형 그리기
'''
import turtle

win=turtle.Screen()
t = turtle.Turtle('turtle')

t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
win.mainloop()
'''
## Mission2-3: 별모양 그리기

import turtle

win=turtle.Screen()
t = turtle.Turtle('turtle')
t.forward(100)
t.right(144)
t.forward(100)
t.left(72)
t.forward(100)
t.right(144)
t.forward(100)
t.left(72)
t.forward(100)
t.right(144)
t.forward(100)
t.left(72)
t.forward(100)
t.right(144)
t.forward(100)
t.left(72)
t.forward(100)
t.right(144)
t.forward(100)
t.left(72)
win.mainloop()