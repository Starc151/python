import math


def task2():
    num = int(input('Введите число: '))
    data = []
    for i in range(1, num+1, 1):
        data.append(math.factorial(i))
    print(data)
task2()