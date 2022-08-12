# 프로그래머스 소수 만들기

from itertools import combinations

def check(a, b, c):
    total = a + b + c
    for i in range(3, total):
        if total % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A:
        if check(i[0], i[1], i[2]):
            answer += 1
    return answer