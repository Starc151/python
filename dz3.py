from audioop import reverse
import math
import random
def createList():
    num = int(input("Введите чило элементов списка: "))
    data = []
    for i in range(0, num, 1):
        data.append(random.randint(0, 10))
    print(f"Полученный список: {data}")
    return data

def task1():
    data = createList()
    sum = 0
    for i in range(len(data)):
        if i%2 != 0:
            sum += data[i]
    print(f"Сумма элеентов с нечетной позицией равноа: {sum}")

def task2():
    data = createList()
    data2 = []
    for i in range(math.ceil(len(data)/2)):
        data2.append(data[i]*data[-i-1])
    print(f"Произведения пар чисел исходного списка: {data2}")

def task3():
    # Решение без строк
    data = createList()
    dataFloat =[]
    for i in range(len(data)):
        data[i] = data[i] + random.random()
        data[i] = round(data[i], 2)
        dataFloat.append(data[i]%1)
        dataFloat[i] = round(dataFloat[i], 2)
    print(f"Случайный список с  дробной частью: {data}")
    print(f"Список без целой части: {dataFloat}")
    r = round(max(dataFloat) - min(dataFloat), 2)
    print(f"Разница между макс и мин значением дробной части элементов: {r}")

def task4():
    num = int(input('Введите число: '))
    print(f"Это число в двоичной системе: {bin(num)[2:]}")

def task5():
    # F(−n) = (−1)**(n+1)*Fn
    num = int(input('Введите число: '))
    fibList0toN = [0]
    for i in range(1, num+1):
        fibList0toN.append(fib(i))
    print(f"Ряд Фибоначчи по числу {num}: {fibList0toN}")

    fibListNto1 = []
    for i in range(len(fibList0toN)-1):
        fibListNto1.append(fibList0toN[i+1])
        if i%2!=0:
            fibListNto1[i]*= -1
    print(fibListNto1)
    fibListNto1.reverse()
    fibList = fibListNto1 + fibList0toN
    print(f"Ряд Негафибоначчи по числу {num}: {fibList}")

def fib(num):
    # F(−n) = (−1)**(n+1)*Fn
    if num in [1, 2]:
        return 1
    else:
        return fib(num-2) + fib(num-1) 
    

# task1()
# task2()
# task3()
# task4()
# task5()
