## 프로그래머스 모의고사

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자가 맞은 수를 기록하는 배열
    cnt = [0, 0, 0]

    # 입력받은 답안을 토대로 각 수포자가 얼마나 맞았는지 탐색
    for i in range(len(answers)):
        # 수포자 1은 5를 주기로 반복
        if answers[i] == one[i % 5]:
            cnt[0] += 1
        # 수포자 2는 8을 주기로 반복
        if answers[i] == two[i % 8]:
            cnt[1] += 1
        # 수포자 3은 10을 주기로 반복
        if answers[i] == three[i % 10]:
            cnt[2] += 1

    # 가장 많이 맞춘 수
    max_cnt = max(cnt)

    # 가장 많이 맞춘 사람을 배열에 담기
    for i in range(3):
        # 가장 많이 맞춘 수와 같은 cnt 요소의 인덱스를 +1 하여 answer에 담기
        if max_cnt == cnt[i]:
            answer.append(i + 1)

    return answer

##############################################################################

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []
    
    for idx, answer in enumerate(answers):
    	if answer == pattern1[idx%len(pattern1)]:
        	score[0] += 1
    	if answer == pattern2[idx%len(pattern2)]:
        	score[1] += 1
    	if answer == pattern3[idx%len(pattern3)]:
        	score[2] += 1   
    for idx, s in enumerate(score):
    	if s == max(score):
        	result.append(idx+1)
    return result