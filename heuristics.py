#!/Users/srossi/Documents/venv/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np

puzzle = np.array([[2, 4, 6, 1],
                   [3, 7, 8, 10],
                   [0, 5, 15, 12],
                   [9, 11, 13, 14]])
solution = np.array([[2, 4, 6, 5],
                    [3, 7, 8, 12],
                    [0, 13, 15, 10],
                    [9, 1, 11, 14]])

solution2 = np.array([[1, 4, 6, 2],
                   [3, 7, 8, 10],
                   [0, 5, 15, 12],
                   [9, 11, 13, 14]])


def count_bad_values(grid, solution):
    eq_values = np.logical_and(True, grid == solution)
    print("size array : ", len(grid)**2)
    return len(grid)**2 - np.count_nonzero(eq_values)

def manhattan_dist(x1, y1, x2, y2):
    return np.abs(x2 - x1) + np.abs(y2 - y1)

def sq_euclidian_dist(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2   

def calc_sum_dist(function, size, puzzle, solution):
    sum = 0
    for x in range(size*size):
        point1 = np.where(puzzle == x)
        point2 = np.where(solution == x)
        sum += function(point1[0][0], point1[1][0], point2[0][0], point2[1][0])
    return sum


# count_good_values(puzzle, solution)
# print (sq_euclidian_dist(1,1,3,3))
# print (manhattan_dist(1,1,3,3))
#
# print ("sum: ", sum_manhattan_dist(4, puzzle, solution2))
print ("manhattan dist: ", calc_sum_dist(manhattan_dist, 4, puzzle, solution2))
print ("euclidian dist: ", calc_sum_dist(sq_euclidian_dist, 4, puzzle, solution2))
print ("bad values dist: ", count_bad_values(puzzle, solution2))
# result = np.where(puzzle == 5)
# print(result)
# print(result[0][0])
# print(result[1][0])