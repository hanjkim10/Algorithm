## 프로그래머스 제일 작은 수 제거

def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr) == 0:
        arr.append(-1)
    return arr