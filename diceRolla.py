#2 dice roll probability chart (selectable amount of trials)

import matplotlib.pyplot as plt
import random
import numpy as np

#take the number of trials
#simulate dice rolls
def rollDie():
    outcomes = {
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0,
        '11':0,
        '12':0
    }
    trials = int(input('Number of trials: '))
    
    for x in range(1, trials):
        outcome = random.randint(1, 6) + random.randint(1, 6)
        outcomes[str(outcome)] += 1
    return outcomes

#graph the outcome
def graph(outcomes):
    xa = np.array([])
    xb = []
    for i in outcomes.keys():
        xb.append(i)
    else:
        x = np.concatenate((xa, xb))
    ya = np.array([])
    yb = []
    for i in outcomes.values():
        yb.append(i)
    else:
        y = np.concatenate((ya, yb))
    plt.bar(x, y)
    plt.title('Number of Times Rolled per Outcome')
    plt.xlabel('Number rolled')
    plt.ylabel('Number of Times Rolled')
    plt.show()

graph(rollDie())