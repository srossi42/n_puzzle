import fileinput

import numpy as np
import math as math

state = None
g = 0
h = 0
parent = None
size = 0
X_position = 0
verbose = False 
debug = False
tempo = 0
sys = None

puzzle = np.array([1,8,2,0,4,3,7,6,5])
X_position = 4
#puzzle = np.array([13,2,10,3,1,12,8,4,5,0,9,6,15,14,11,7])
#X_position = 10
#puzzle = np.array([6,13,7,10,8,9,11,0,15,2,12,5,14,3,1,4])
#X_position = 8
#puzzle = np.array([3,9,1,15,14,11,4,6,13,0,10,12,2,7,8,5])
#X_position = 10

size = len(puzzle)

# Compte le nombre d'inversions pour trier le tableau (eg. [2,3,1] = 2)
def count_inversion(puzzle):
    inversion = 0
    index = 0
    index_next = 0
    while index < len(puzzle) - 1:
        if puzzle[index + 1] == 0:
            index_next = index + 2
        else:
            index_next = index + 1
        if puzzle[index] > puzzle[index_next]:
            inversion += 1
            puzzle[index], puzzle[index_next] = puzzle [index_next], puzzle[index]
            index = 0
        else:
            index += 1
    return inversion % 2

# Vérifie la position de X su une ligne paire ou impaire en partant de la dernière ligne
def check_X_position():
    position = (size - X_position + 1)
    if position % math.sqrt(size) == 0 :
        line = position // math.sqrt(size)
    else :
        line = position // math.sqrt(size) + 1
    return line % 2

# Vérifie si le tableau est pair ou impaire et les conditions associées (position de X et nbre d'inversions)
def check_if_solvable(puzzle):
    if (size % 2 == 1) and count_inversion(puzzle) == 0 :
        return 1
    elif (size % 2 == 0) and count_inversion(puzzle) != check_X_position() :
        return 1
    return 0

print (check_if_solvable(puzzle))