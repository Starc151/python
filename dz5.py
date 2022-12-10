import random
import sys
from tkinter import *

root = Tk()
root.title('Крестики и Нолики')
root.geometry('440x440')

games = Canvas(root, width='390', height='390', bg='red')
games.place(x=25, y=25)
for i in range(0, 9):
    x = i // 3 * 130
    y = i % 3 * 130
    games.create_rectangle(x+3, y+3, x + 130, y + 130,
                                        width = 3,
                                        outline = '#A5A5A5',
                                        fill = '#CCCCCC',
                                        activefill = '#FFFAFA')


root.mainloop()
# def gameXO():
#     mapping = ['_']*9
#     freePosition = list(range(0, 9))
#     mapGame = list(range(1, 10))
#     mapGame = "".join(map(str, mapGame))
#     move = random.randint(0,1)
#     print("Карта игры:")
#     printList(mapGame)
#     selectDifficulty()
#     move1 = human
#     move2 = comp
#     if move == 1:
#         print("Вы ходите первым")
#     else:
#        print("Первым ходит компьютер")
#        move1, move2 = move2, move1

#     for i in range (len(freePosition)):
#         move1(mapping, freePosition)
#         if len(freePosition) == 0:
#             print("Ничья")
#             sys.exit()
#         move2(mapping, freePosition)

# def selectDifficulty():
#     global difficulty
#     difficulty = 0
#     difficulty = input('Выберите сложность от 0, 1 или 2: ')
#     if difficulty.isalpha():
#         print("Так играть компюьтер не сможет")
#         return selectDifficulty()
#     difficulty = int(difficulty)
#     if 0 > difficulty or difficulty > 2:
#         print("Так играть компюьтер не сможет")
#         return selectDifficulty()

# def printList(list):
#         print("|".join(list)[:5])
#         print("|".join(list)[6:11])
#         print("|".join(list)[12:].replace('_', ' '))

# def human(mapping, freePosition):
#     pos = input('Куда поствить "x"? ')
#     if pos.isalpha():
#         print('Введите число!')
#         return human(mapping, freePosition)
#     pos = int(pos)-1   
#     if 9 <= pos or pos < 0:
#         print('Недопустимое значение!')
#         return human(mapping, freePosition)
#     if mapping[pos] != '_':
#         print('Это меcто уже занято!')
#         return human(mapping, freePosition)
#     mapping[pos] = 'x'
#     freePosition.remove(pos)
#     printList(mapping)
#     victory(mapping, 'x')

# def comp(mapping, freePosition):
#     print("Ход компьютера...")
#     dlp = random.choice(freePosition)
#     v = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
#     random.shuffle(v)
#     if difficulty == 2:
#         for i in v:
#             if mapping[i[0]] == mapping[i[1]] == 'x' and mapping[i[2]] == '_':
#                 dlp = i[2]
#             elif mapping[i[0]] == mapping[i[2]] == 'x' and mapping[i[1]] == '_':
#                 dlp = i[1]
#             elif mapping[i[1]] == mapping[i[2]] == 'x' and mapping[i[0]] == '_':
#                 dlp = i[0]
#     if difficulty > 1:
#         for i in v:
#             if mapping[i[0]] == mapping[i[1]] == 'o' and mapping[i[2]] == '_':
#                 dlp = i[2]
#             elif mapping[i[0]] == mapping[i[2]] == 'o' and mapping[i[1]] == '_':
#                 dlp = i[1]
#             elif mapping[i[1]] == mapping[i[2]] == 'o' and mapping[i[0]] == '_':
#                 dlp = i[0]
#     mapping[dlp] = 'o'
#     freePosition.remove(dlp)
#     printList(mapping)
#     victory(mapping, 'o')

# def victory(mapping, s):
#     v = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
#     for i in v:
#         if s == mapping[i[0]] == mapping[i[1]] == mapping[i[2]]:
#             if s == 'x':
#                 print("Вы победили!")
#                 sys.exit()
#             elif s == 'o':
#                print("Победил коспьютер!") 
#                sys.exit()

# gameXO()