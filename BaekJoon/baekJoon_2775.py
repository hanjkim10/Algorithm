n = int(input())

for i in range(n):
    floor = int(input())
    room_num = int(input())
    people = [i for i in range(1, room_num + 1)]

    for x in range(floor):
        new = []
        for y in range(room_num):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
    print(people[-1])