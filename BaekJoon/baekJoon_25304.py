k = int(input())
n = int(input())

x = 0

for i in range (n) :
    a, b = map(int, input().split())
    c = a*b
    x = x + c
    
if k == x :
    print("Yes")
else :
    print("No")