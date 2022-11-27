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
    print(sum(data))

def task4():
    mult = 1
    num = int(input('Введите число: '))
    data = []
    for i in range(-num, num+1, 1):
        data.append(i)
    print(f"Получившийся список: {data}")
    f = open('forDZ2.txt', 'r').read().split('\n')
    positionData = []
    if int(f[-1]) >= len(data):
        print("Введите число побольше!")
        return False
    for i in f:
        mult *= data[int(i)]
        positionData.append(i)
    print(f"Список позиций из файла: {positionData}") # в фвйле forDZ2.txt
    print(f"Произведение элементов на указанных позициях: {mult}")

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
task4()
# task5()