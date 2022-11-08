#generates simple battleship board
import numpy as np
import random as rd
import math

def genShape(board, sNum):
    while True:
        x, y = rd.randint(0, int(len(board) - 2 - math.ceil(sNum/2))), rd.randint(0, int(len(board[0]) - math.ceil(sNum/2)))
        free = True
        locarr = []
        for i in range(sNum):
            if i % rd.randint(2, 3) == 0:
                X = x + 1
            else: X = x
            Y = y + int(i / 2)
            if (board[X][Y] != " "):
                free = False
            locarr.append([X, Y])
        if free:
            for loc in locarr:
                board[loc[0]][loc[1]] = "#"
            break
        break

def genMap():
    board = np.empty([20, 30]).astype(np.str_)

    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] = " "

    for x in range(50):
        sNum = rd.randint(1, len(board) - 1)
        genShape(board, sNum)

    return board

def mapTester(iter):
    for x in range(iter):
        try:
            genMap()
        except:
            print("uh oh")

# mapTester(100)

map = genMap()
for x in map:
    for y in x:
        print(str(y) + " ", end="")
    print()
