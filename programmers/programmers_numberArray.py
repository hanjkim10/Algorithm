## 프로그래머스 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i) 
    new_ans = sorted(answer)
    return new_ans if new_ans else [-1]