n = int(input())
key = n
count = 0

while True:
    count += 1
    sum = n // 10 + n % 10
    n = n % 10 * 10 + n % 10
    if(n == key):
        break
print(count)