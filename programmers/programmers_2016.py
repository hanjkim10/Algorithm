## 프로그래머스 2016

date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a-1])+b-1)%7] 
    return answer