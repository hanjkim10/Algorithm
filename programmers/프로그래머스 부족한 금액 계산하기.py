## 프로그래머스 부족한 금액 계산하기

price = 3
money = 20
count = 4
result = 10
answer = []

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))