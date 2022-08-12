## 프로그래머스 정수 내림차순으로 배치하기

def solution(n):
    n = list(str(n)) 
    n.sort(reverse=True) 
    return int("".join(n))