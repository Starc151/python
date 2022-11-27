import math
import random


def task2():
    num = int(input('Введите число: '))
    data = []
    for i in range(1, num+1, 1):
        data.append(math.factorial(i))
    print(data)

def task3():
    num = int(input('Введите число: '))
    data = []
    for i in range(1, num+1, 1):
        data.append((1+1/i)**i)
    print(data)

def task5():
    num = int(input('Введите число: '))
    data = []
    for i in range(-num, num+1, 1):
        data.append(i)
    print(data)
    random.shuffle(data)
    print(data)
# task2()
# task3()
# task5()