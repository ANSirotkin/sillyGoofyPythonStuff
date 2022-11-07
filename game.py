#game w/ randomly generated map
import numpy as np
import random as rd
import mapGen as mgen

def game():
    map = mgen.genMap()
    print(map)

def gLoop():
    pass

game()
