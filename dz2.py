import math
import random
def task1():
    sum = 0
    num = input('Введите число: ')
    for i in num:
# если if написать в 1 условие if i != "." or "-", то почему-то выдает ошибку
# припроверке на условие, укзанное вторым?
        if i != ".":
            if i != "-":
                sum += int(i)
        
    print(sum)


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

# task1()
# task2()
# task3()
# task5()