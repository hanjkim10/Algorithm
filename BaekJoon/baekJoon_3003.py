listc = list(map(int, input().split()))
temp = []
answer = 0
setc = [1, 1, 2, 2, 2, 8]
result = [0, 0, 0, 0, 0, 0]


for i in listc:
    temp.append(i)
    
for j in range(len(temp)):
    if temp[j] == setc[j]:
        result[j] = 0
    if temp[j != setc[j]]:
        result[j] = setc[j] - temp[j]

answer = ' '.join(map(str,result))
print(answer)