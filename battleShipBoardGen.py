#generates simple battleship board
import numpy as np
import random as rd

#4 ships
    #1 Carrier : 2x3 (shipNum 6)
    #2 Battleship : 2x2 (shipNum 4)
    #1 Cruiser : 2x1 (shipNum 2)

def genShip(board, shipNum):
    letter = {
        6: "X",
        4: "O",
        2: "A"
    }
    while True:
        x, y = rd.randint(0, 8), rd.randint(0, 8)
        if x > 7 or y > 6:
            continue
        free = True
        locarr = []
        for i in range(shipNum):
            if i % 2 == 0:
                X = x + 1
            else: X = x
            Y = y + int(i / 2)
            if (board[X][Y] != " "):
                free = False
                continue
            locarr.append([X, Y])
        if free:
            for loc in locarr:
                board[loc[0]][loc[1]] = letter[shipNum]
            break

def genBoard():
    board = np.empty([9, 9])
    board = board.astype(np.str_)

    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] = " "
    
    genShip(board, 6)
    genShip(board, 4)
    genShip(board, 4)
    genShip(board, 2)

    return board