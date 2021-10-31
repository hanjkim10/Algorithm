## 프로그래머스 문자열 내 p와 y의 개수

def solution(s):
    return s.lower().count('p') == s.lower().count('y')

def solution(s):
    answer = True
    p = 0
    y = 0

    for i in s:
        if i == 'p' or i =='P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    
    if p != y:
        answer = False