import random
import sys
difficulty  = 0
def gameXO():
    mapping = ['_']*9
    freePosition = list(range(0, 9))
    mapGame = list(range(1, 10))
    mapGame = "".join(map(str, mapGame))
    move = random.randint(0,1)
    print('Игра в крестики-нолики')
    print("Карта игры:")
    printList(mapGame)
    global difficulty
    difficulty = int(input('Выберите сложность от 0 до 1: '))
    move1 = human
    move2 = comp
    if move == 1:
        print("Вы ходите первым")
    else:
       print("Первым ходит компьютер")
       move1, move2 = move2, move1

    for i in range (len(freePosition)):
        move1(mapping, freePosition)
        if len(freePosition) == 0:
            print("Ничья")
            sys.exit()
        move2(mapping, freePosition)
        
        


def printList(list):
        print("|".join(list)[:5])
        print("|".join(list)[6:11])
        print("|".join(list)[12:].replace('_', ' '))

def human(mapping, freePosition):
    pos = int(input('Куда поствить "x"? '))-1
    if 9 <= pos or pos < 0:
        print('Недопустимое значение!')
        return human(mapping, freePosition)
    if mapping[pos] != '_':
        print('Это меcто уже занято!')
        return human(mapping, freePosition)
    mapping[pos] = 'x'
    freePosition.remove(pos)
    printList(mapping)
    victory(mapping, 'x')

def comp(mapping, freePosition):
    print("Ход компьютера...")
    dlp = random.choice(freePosition)
    if difficulty == 1:
        v = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        random.shuffle(v)
        for i in v:
            if   mapping[i[0]] == mapping[i[1]] and mapping[i[2]] == '_':
                dlp = i[2]
            elif mapping[i[0]] == mapping[i[2]] and mapping[i[1]] == '_':
                dlp = i[1]
            elif mapping[i[1]] == mapping[i[2]] and mapping[i[0]] == '_':
                dlp = i[0]

    mapping[dlp] = 'o'
    freePosition.remove(dlp)
    printList(mapping)
    victory(mapping, 'o')

def victory(mapping, s):
    v = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in v:
        if s == mapping[i[0]] == mapping[i[1]] == mapping[i[2]]:
            if s == 'x':
                print("Вы победили!")
                sys.exit()
            elif s == 'o':
               print("Победил коспьютер!") 
               sys.exit()

gameXO()