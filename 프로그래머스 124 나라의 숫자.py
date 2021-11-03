## 프로그래머스 124 나라의 숫자

def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

def solution(n):
    array = ['1','2','4']
    if n <= 3:
        return array[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + array[r]
