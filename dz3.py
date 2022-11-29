import math
import random
def createList():
    num = int(input("ВВедите чило элементов списка: "))
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

# task1()
# task2()
