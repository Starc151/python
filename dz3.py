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

# task1()
# task2()
# task3()
