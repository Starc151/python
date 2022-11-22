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

# task1()
# task3()
