## 프로그래머스 핸드폰 번호 가리기

def solution(phone_number):
    for i in range(len(phone_number)-4):
        phone_number = phone_number.replace(phone_number[i], '*', 1)
    return phone_number

def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4:]