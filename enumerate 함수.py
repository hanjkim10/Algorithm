## 리스트가 있는 경우 순서와 리스트의 값을 전달하는 함수
## 순서가 있는 자료형 (list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포한하는 enumerate 객체 리턴
## 보통 enumerate 함수는 for문과 함께 자주 사용

## ex 1)
test = [1, 2, 3]
for index, value in enumerate(test):
    print(index, value)

## ex 2)
a = ['name', 'python', 'type', 'snake']
c = {}
for i, name in enumerate(a):
    c[i] = a[i]
print(c)

