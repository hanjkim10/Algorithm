## 프로그래머스 k번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        first_sorting_array = array[command[0] - 1:command[1]]
        first_sorting_array.sort()
        answer.append(first_sorting_array[command[2] - 1])
    
    return answer