m = int(input())
n = int(input())

prime_number_list = []
for num in range(m, n+1): 
    count = 0 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0: 
                count += 1 
                break
        if count == 0: 
            prime_number_list.append(num)

if len(prime_number_list) > 0:
    print(sum(prime_number_list))
    print(min(prime_number_list))
else:
    print(-1)