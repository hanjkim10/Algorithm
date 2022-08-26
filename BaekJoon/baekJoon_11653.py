N = int(input())
d = 2

while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)

        
n = int(input())
i = 2
while n!= 1:
    if n % i == 0:
        n = n / i
        print(i)
    else: 
        i += 1