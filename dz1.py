def task1():
    numDay = int(input('Введите день недели: '))
    if 0 < numDay < 6:
        print('нет')
    elif 5 < numDay < 8:
        print('да')
    else :
        print('нет такого дня')

task1()
