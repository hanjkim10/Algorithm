## 프로그래머스 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    return sorted(list({x + y for x, y in combinations(numbers, 2)}))