## 람다 함수 = 익명 함수
## 코드의 간결함 메모리의 절약


## python lambda 함수와 map
# 1. 일반 함수 버전
def plus_two(x):
    return x + 2

result_1 = list(map(plus_two, [1, 2, 3, 4, 5]))
print(result_1)
# -> [3, 4, 5, 6, 7]

# 2. 람다 함수 버전
result_2 = list(map(lambda x: x + 2), [1, 2, 3, 4, 5])
print(result_2)
# -> [3, 4, 5, 6, 7]


## python lambda 함수와 ilter
# 1. 일반 함수 버전
def is_even(x):
    return x & 2 == 0

result_3 = list(filter(is_even, range(10)))
print(result_3)
# -> [0, 2, 4, 6, 8]

# 2. 람다 함수 버전
result_4 = list(filter(lambda x: x % 2 == 0), range(10))
print(result_4)
# -> [0, 2, 4, 6, 8]

