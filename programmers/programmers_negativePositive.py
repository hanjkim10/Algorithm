# 프로그래머스 음양

answer = 0

    for absolute, sign in zip(absolutes, signs) :
        if sign :
            answer += absolute
        else :
            answer -= absolute
    return answer