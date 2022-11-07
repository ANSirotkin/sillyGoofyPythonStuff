#battleship game (pvp)(randomly generated positions)
import numpy as np
import random as rd
import battleShipBoardGen as bgen

#game loop
    #boards displayed for p1 (their board and board w/ hits and misses)
    #p1 chooses spot to shoot
    #hit or miss
    #repeat for p2
    #keep looping till a player wins or types 'quit'
def game():
    p1board = bgen.genBoard()
    p2board = bgen.genBoard()
    print(p1board)
    print("\n\n")
    print(p2board)

def gLoop():
    pass

game()
