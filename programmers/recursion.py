from tkinter import N
from unittest import result


1. 
const = '일정값'
def fucntion(input):
    if input > const: # 입력이 일정 값 이상이면
        return function(input - 1) # 입력보다 작은 값
    else:
        return const, input, # 또는 문제에서 주어지는 특정 값 # 재귀 호출 종료
    
2.
const = '일정값'
def function(input):
    if input <= const: # 입력이 일정 값 이하면
        return const, input, # 또는 문제에서 주어지는 특정 값
    function('') # 입력보다 작은 값
    return result

# EX.1
def factorial(x):
    if x > 1:
        return x * function(x - 1)
    else:
        return x

# EX.2
def factorial2(num):
    if num > 1:
        return num * factorial2(num - 1)
    return num

# FIBO
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    