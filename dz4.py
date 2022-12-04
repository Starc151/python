import math
import random
import sympy
import dz3
from sympy import *

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

def task4():
    k = int(input("Введите натуральную степень k: "))
    listKoef = [random.randint(0, 101) for i in range(k+1)]
    print(f"Список случайных коэффициентов: {listKoef}")
    ln = len(listKoef)
    polynom = ""
    for i in range(ln):
        if ln-1-i == 1:
            polynom += str(listKoef[i])+'x+'
        elif ln-1-i == 0:
            polynom += str(listKoef[i])
        else:
            polynom += str(listKoef[i])+'x**'+str(ln-1-i)+'+'
    print(f"Многочлен степени {k}: {polynom}")
    with open('forDz4Task4.txt', 'w') as data:
        data.write(polynom)

def task5():
    x = sympy.Symbol('x')
    m1 = open('task5_1.txt', 'r')
    m2 = open('task5_2.txt', 'r')
    exp1 = sympy.sympify(*m1)
    exp2 = sympy.sympify(*m2)
    print(exp1 + exp2)

# task1()
# task2()
# task3()
task4()
# task5()