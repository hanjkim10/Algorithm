## 프로그래머스 체육복

def solution(n, lost, reserve):
    count = n - len(lost)
    for i in lost:
        if i - 1 or i + 1 in lost:
            count += 1