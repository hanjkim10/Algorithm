A, B = map(int, input().split())
C = int(input())

i = C // 60
j = C % 60

new_A = A + i
new_B = B + j

if new_B >= 60:
    new_B = new_B - 60
    new_A = new_A + 1
    
if new_A > 23:
    new_A = new_A - 24

result = (new_A, new_B)
new_result = (' '.join(map(str, result)))
print(new_result)