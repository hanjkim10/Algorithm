# 프로그래머스 없는 숫자 더하기

def solution(numbers):
    example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    for i in numbers:
        if i in example:
            example.remove(i)
    return sum(example)