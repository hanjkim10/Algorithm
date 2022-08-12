## 프로그래머스 체육복

def solution(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)
    
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
    return n - len(new_lost)