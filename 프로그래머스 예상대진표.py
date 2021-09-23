## 프로그래머스 예상대진표

def solution(n,a,b):
    count = 0

    while a != b:
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        count += 1

    return count