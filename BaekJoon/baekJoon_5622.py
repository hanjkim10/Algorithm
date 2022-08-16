alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ip = input()
ip_list = list(ip)
# print(ip_list)
temp = 0
cnt = []

for i in ip_list:
    for j in range(len(alp)):
        if i in alp[j]:
            count = int(j + 3)
            cnt.append(count)
result = sum(cnt)
print(result)