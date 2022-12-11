import random
import sys
import time
from tkinter import *
import tkinter.messagebox

game = tkinter.Tk()
game.title('Крестики и Нолики')
game.geometry('440x440')

firstMove = random.randint(0, 1)
if firstMove == 0:
    tkinter.messagebox.showinfo("", "Первым ходите вы")
else:
    tkinter.messagebox.showinfo("", "Первым ходит компьютер")

mapGame = Canvas(game, width='390', height='390', bg='orange')
mapGame.place(x=25, y=25)
for i in range(0, 9):
    x = i // 3 * 130
    y = i % 3 * 130
    mapGame.create_rectangle(x+3, y+3, x + 130, y + 130,
                                        width = 3,
                                        outline = '#A5A5A5',
                                        fill = '#CCCCCC',
                                        activefill = '#FFFAFA')

statusGame = ['_']*9
freePosition = list(range(0, 9))
v = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def victory(s):
    print()
    for i in v:
        if s == statusGame[i[0]] == statusGame[i[1]] == statusGame[i[2]]:
            if s == 'x':
                tkinter.messagebox.showinfo("", "Победа за вами")
                game.destroy()
            elif s == 'o':
               tkinter.messagebox.showinfo("", "Победа за компьютером")
               game.destroy()
    # if statusGame.count('_') == False:
    #     tkinter.messagebox.showinfo("", "Ничья")
    #     game.destroy()

def compMove():
    cp = random.choice(freePosition)
    for i in v:
        if statusGame[i[0]] == statusGame[i[1]] == 'o' and statusGame[i[2]] == '_':
            cp = i[2]
            break
        elif statusGame[i[0]] == statusGame[i[2]] == 'o' and statusGame[i[1]] == '_':
            cp = i[1]
            break
        elif statusGame[i[1]] == statusGame[i[2]] == 'o' and statusGame[i[0]] == '_':
            cp = i[0]
            break
        elif (statusGame[i[0]] == statusGame[i[1]] == 'x') and statusGame[i[2]] == '_':
            cp = i[2]
            break
        elif (statusGame[i[0]] == statusGame[i[2]] == 'x') and statusGame[i[1]] == '_':
            cp = i[1]
            break
        elif (statusGame[i[1]] == statusGame[i[2]] == 'x') and statusGame[i[0]] == '_':
            cp = i[0]
            break
        elif statusGame[i[0]] == 'o' and (statusGame[i[1]] == statusGame[i[2]] == '_'):
            cp = i[1]
            break
        elif statusGame[i[2]] == 'o' and (statusGame[i[0]] == statusGame[i[1]] == '_'):
            cp = i[1]
            break
        elif statusGame[0] == '':
            cp = 0
            break
        elif statusGame[6] == '':
            cp = 6
            break
        elif statusGame[2] == '':
            cp = 3
            break
        elif statusGame[8] == '':
            cp = 8
            break
        elif statusGame[4] == '_':
            cp = 4
    col = cp % 3
    row = cp // 3
    x = 25 + 130 * col
    y = 25 + 130 * row
    mapGame.create_oval(x, y, x + 80, y + 80, width = 10, outline = '#CC5500')
    statusGame[cp]  = "o"
    victory('o')
    freePosition.remove(cp)

if firstMove == 1:
    compMove()

def humanMove(event):
    col = event.x // 130
    row = event.y // 130
    index = col + row * 3
    if statusGame[index] == '_':
        x = 25 + 130 * col
        y = 25 + 130 * row
        mapGame.create_line(x, y, x + 80, y + 80, width=10, fill='green')
        mapGame.create_line(x, y + 80, x + 80, y, width=10, fill='green')
        statusGame[index]  = "x"
        victory('x')
        freePosition.remove(index)
        game.after(500, compMove)


    


mapGame.bind('<Button-1>', humanMove)
game.mainloop()
# def gameXO():
#     mapping = ['_']*9
#     freePosition = list(range(0, 9))
#     move = random.randint(0,1)
#     print("Карта игры:")
#     printList("".join(map(str, list(range(1, 10)))))
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

# gameXO()