# 프로그래머스 없는 숫자 더하기

def solution(numbers):
    example = list(range(0,10))
    
    for i in numbers:
        if i in example:
            example.remove(i)
    return sum(example)