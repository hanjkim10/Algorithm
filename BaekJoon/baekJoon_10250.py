n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())
    room_num = n // h + 1
    floor = n % h
    
    if floor == 0:
        floor = h
        room_num -= 1
        
    print(floor * 100 + room_num)