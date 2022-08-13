## 프로그래머스 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers)) # 사전 값으로 정렬하기
    numbers.sort(key=lambda x: x * 3, reverse=True) # number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    
    return str(int(''.join(numbers)))
    # numbers = [0, 0, 0, 0] 이면 0이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 str로 변환해야 한다.