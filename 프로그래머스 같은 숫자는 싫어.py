## 프로그래머스 같은 숫자는 싫어.py

def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)
    return answer