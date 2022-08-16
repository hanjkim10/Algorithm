ip = input().lower()
ip_list = list(set(ip))
cnt = []

for i in ip_list:
    count = ip.count(i)
    cnt = cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(ip_list[(cnt.index(max(cnt)))].upper())