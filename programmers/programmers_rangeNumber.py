# 프로그래머스 내적

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        num = a[i] * b[i]
        answer = num + answer
    return answer