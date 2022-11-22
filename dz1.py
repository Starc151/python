def task1():
    numDay = int(input('Введите день недели: '))
    if 0 < numDay < 6:
        print('нет')
    elif 5 < numDay < 8:
        print('да')
    else :
        print('нет такого дня')

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


# task1()
# task3()
# task4()
task5()
