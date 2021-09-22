import sys

x, n = map(int, sys.stdin.readline().split())

result = []

for i in range(1, n+1):
    result.append(x * i)
return result