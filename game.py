#game w/ randomly generated map
import numpy as np
import random as rd
import mapGen as mgen

def game():
    for x in range(3):
        print(mgen.genMap())
        print("\n\n")

def gLoop():
    pass

game()
