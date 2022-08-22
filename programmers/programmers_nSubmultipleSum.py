## 프로그래머스 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer

## 어떤 수의 ½승이 정수면 그 수는 약수의 개수가 홀수이다. 
## ex) 4½ 의 약수의 개수는 1, 2, 4이다.
## ex) 16½ 의 약수의 개수는 1, 2, 4, 8, 16이다.