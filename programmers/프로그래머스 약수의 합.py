##프로그래머스 약수의합

def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])