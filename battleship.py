#battleship game (pvp)(randomly generated positions)
from contextlib import nullcontext
from queue import Empty
import numpy as np
import random as rd

#5 diff battleships:
    #Carrier (5)
    #Battleship (4)
    #Cruiser (3)
    #Sub (3)
    #Destroyer (2)

boardP1 = np.empty([9, 9])
boardP2 = np.empty([9, 9])
boardShownP1 = []
boardShownP2 = []
#generate boards for both players (9x9)
    #2 boards for each player
        #1 board for their own battleships
        #1 board showing hits and misses against opponent
def genCarrier():
    while True:
        location = [rd.randint(0, 8), rd.randint(0, 8)]
        rotation = rd.randint(1, 4)
def genBattleship():
    pass
def genCruiser():
    pass
def genSub():
    pass
def genDestroyer():
    pass
def genBoard():
    pass

#game loop
    #boards displayed for p1 (their board and board w/ hits and misses)
    #p1 chooses spot to shoot
    #hit or miss
    #repeat for p2
    #keep looping till a player wins or types 'quit'
def game():
    pass

def gLoop():
    pass
