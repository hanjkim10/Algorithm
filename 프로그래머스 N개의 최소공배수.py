arr = [2, 6, 8, 14]

# def solution(arr):
a = arr.sort(reverse=True)

print(a)
# for i in range(len(arr)-1):
#     a = arr[i]
#     b = arr[i+1]
#     while a%b:
#         r = a%b
#         a = b
#         b = r
#     arr[i+1] = (arr[i]*arr[i+1])/b

# return arr[-1]