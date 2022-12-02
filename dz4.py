import math
import dz3

def task1():
    d = float(input('Введите число для определения точности: '))
    d  = str(d)
    d = len(d)
    t = str(math.pi)
    t = t[:2]
    s = str(math.pi)
    s = s[2:d]
    print(f"Число Пи c заданной точностью d: {t+s}")

def task2():
    num = int(input('Введите число для вычисления простых множителей: '))
    endList = []
    for i in range(2, num + 1):
        if num % i == 0:
            count = 1
            for j in range(2, (i // 2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                endList.append(i)
    print(endList)

def task3():
    list = dz3.createList()
    newList = []
    for i in list:
        if list.count(i) == 1:
            newList.append(i)
    print(f"Список неповторяющихся элементов: {newList}")

task1()
# task2()
# task3()