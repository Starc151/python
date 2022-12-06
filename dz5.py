import random


def task2():
    mapping = ['_']*9
    position = list(range(1, 10))
    print('Игра в крестики-нолики')
    move = random.randint(0, 1)


    
    if move ==1:
        print("Ваш ход первый")
    else:
        print("Первым ходит компьютер")

    print(position)
    for i in range(0, 9):
        pos = int(input())-1
        mapping[pos] = 'x'
        position.remove(pos+1)
    #     if mapping[o] == ' ':
    #         mapping[o] = 'o'
    
    #     mapping[random.randint(0, 8)] = 'o'
        print("|".join(mapping)[:5])
        print("|".join(mapping)[6:11])
        print("|".join(mapping)[12:].replace('_', ' '))

def human():
    pos = int(input('Укажите место крестика от 1 до 9:'))-1





        # if i != '':
        #     mapping.append(random.randint(1, 5))
        # print("Ваш ход первый")
        #    # Вводится через пробел, наприме
    # else:
    #     print("Компьютер ходит первым")
    # print(mapping)


task2()