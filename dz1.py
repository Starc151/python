def task1():
    numDay = int(input('Введите день недели: '))
    if 0 < numDay < 6:
        print('нет')
    elif 5 < numDay < 8:
        print('да')
    else :
        print('нет такого дня')

def task2():
    # Не уверен, что рпавльно понял, что нужно сделать
    def isEqual(x , y, z):
        # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
        left = not (x or y or z)
        right = not x and not y and not z
        return left == right
    for x in 1, 0:
        for y in 1, 0:
            for z in 1, 0:
                result = isEqual(x, y, z)
                print(f'{x} {y} {z} {result}')


def task3():
    xy = list(map(int, input('Введите X и Y: ').split()))
    x = xy[0]
    y = xy[1]
    if x>0 and y>0:
        print(1)
    elif x<0 and y>0:
        print(2)
    elif x<0 and y<0:
        print(3)
    else:
        print(4)

def task4():
    numQuarter = int(input('введите номер четверти: '))
    match numQuarter:
        case 1: 
            print('Диапазон: x>0, y>0')
        case 2: 
            print('Диапазон: x<0, y>0')
        case 3: 
            print('Диапазон: x<0, y<0')
        case 4: 
            print('Диапазон: x>0, y<0')
        case _:
            print('Такой четверти нет')

def task5():
    aXY = list(map(int, input('ВВедите координаты точки A: ').split()))
    bXY = list(map(int, input('ВВедите координаты точки B: ').split()))
    aX = aXY[0]
    aY = aXY[1]
    bX = bXY[0]
    bY = bXY[1]
    ab = ((bX - aX)**2 + (bY -aY)**2)**0.5
    ab = "{0:.2f}".format(ab)
    print(f'Расстояние между точками А и В: {ab}')


task1()
task2()
task3()
task4()
task5()
