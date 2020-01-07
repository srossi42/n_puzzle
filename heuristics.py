#!/Users/srossi/Documents/venv/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np


def count_bad_values(grid, solution):
    eq_values = np.logical_and(True, grid == solution)
    return len(grid)**2 - np.count_nonzero(eq_values)


def manhattan_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def sq_euclidian_dist(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


def uniform(x1, y1, x2, y2):
    return 0


def calc_heuristic(function, size, puzzle, solution):
    if function == count_bad_values:
        return count_bad_values(puzzle.state, solution)

    start = 0 if size < 4 else 1

    if puzzle.parent is None:
        puzzle.h = 0

        # puzzle.zero_position = np.where(puzzle.state == 0)

        for x in range(start, size*size):
            point1 = np.where(puzzle.state == x)
            point2 = np.where(solution == x)
            puzzle.h += function(point1[0][0], point1[1][0], point2[0][0], point2[1][0])
    else:

        puzzle.h = puzzle.parent.h
        solution_zero = np.where(solution == 0)

        solution_value = np.where(solution == puzzle.parent.state[puzzle.zero_position[0],
                                                                         puzzle.zero_position[1]])

        # parent_zero = np.where(puzzle.parent.state == 0)
        parent_zero = puzzle.parent.zero_position
        value = [parent_zero[0], parent_zero[1]]
        parent_value = np.where(puzzle.parent.state == puzzle.state[value[0], value[1]])
        # curr_zero = np.where(puzzle.state == 0)
        curr_zero = puzzle.zero_position
        curr_value = np.where(puzzle.state == puzzle.state[value[0], value[1]])
        if size < 4:
            puzzle.h -= function(parent_zero[0][0], parent_zero[1][0], solution_zero[0][0], solution_zero[1][0])
            puzzle.h += function(curr_zero[0][0], curr_zero[1][0], solution_zero[0][0], solution_zero[1][0])
        puzzle.h -= function(parent_value[0][0], parent_value[1][0], solution_value[0][0], solution_value[1][0])
        puzzle.h += function(curr_value[0][0], curr_value[1][0], solution_value[0][0], solution_value[1][0])
    return puzzle


def get_heuristic(heuristic_number):
    heuristic_list = [manhattan_dist, sq_euclidian_dist, count_bad_values, uniform]
    return heuristic_list[int(heuristic_number) - 1]
