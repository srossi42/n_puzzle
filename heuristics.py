#!/Users/srossi/Documents/venv/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np


def count_bad_values(grid, solution):
    eq_values = np.logical_and(True, grid == solution)
    print("size array : ", len(grid)**2)
    return len(grid)**2 - np.count_nonzero(eq_values)


def manhattan_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def sq_euclidian_dist(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


def uniform(x1, y1, x2, y2):
    return 0


def calc_heuristic(function, size, puzzle, solution):
    if puzzle.parent is None:
        h_sum = 0
        for x in range(size*size):
            point1 = np.where(puzzle.state == x)
            point2 = np.where(solution == x)
            h_sum += function(point1[0][0], point1[1][0], point2[0][0], point2[1][0])
    else:
        h_sum = puzzle.parent.h
        # print("h_sum avant : ", h_sum)
        solution_zero = np.where(solution == 0)
        # print("solution_zero : ", solution_zero[0][0])
        h_sum -= function(puzzle.parent.zero_position[0], puzzle.parent.zero_position[1],
                           solution_zero[0][0], solution_zero[1][0])
        h_sum += function(puzzle.zero_position[0], puzzle.zero_position[1],
                           solution_zero[0][0], solution_zero[1][0])
    # print("h_sum apres : ", h_sum)
    # exit()
    return h_sum


def get_heuristic(heuristic_number):
    heuristic_list = [manhattan_dist, sq_euclidian_dist, count_bad_values, uniform]
    return heuristic_list[int(heuristic_number) - 1]
