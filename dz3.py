import random


def task1():
    num = int(input("ВВедите чило элементов списка: "))
    data = []
    for i in range(0, num, 1):
        data.append(random.randint(0, 10))
    print(f"Полученный список: {data}")
    sum = 0
    for i in range(len(data)):
        if i%2 != 0:
            sum += data[i]
    print(f"Сумма элеентов с нечетной позицией равноа: {sum}")
task1()