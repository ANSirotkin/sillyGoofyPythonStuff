#generates simple battleship board
import numpy as np
import random as rd
import math

def genShape(board, sNum):
    while True:
        x, y = rd.randint(0, int(len(board) - 1 - math.ceil(sNum/2))), rd.randint(0, int(len(board[0]) - math.ceil(sNum/2)))
        free = True
        locarr = []
        for i in range(sNum):
            if i % 2 == 0:
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
    board = np.empty([15, 15])
    board = board.astype(np.str_)

    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] = " "

    for x in range(20):
        sNum = rd.randint(1, len(board) - 1)
        genShape(board, sNum)

    return board