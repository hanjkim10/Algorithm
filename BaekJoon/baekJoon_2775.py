n = int(input())

for i in range(n):
    floor = int(input())        # 층k
    room_num = int(input())        # 호n
    people = [i for i in range(1, room_num + 1)]     # 0층

    for x in range(floor):
        new = []
        for y in range(room_num):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
        #print(people)		# peaple에 들어있는 값 출력해 봄
    print(people[-1])       # K층 n호