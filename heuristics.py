#!/Users/srossi/Documents/venv/bin/python3.7
# -*- coding: utf-8 -*-

import numpy as np


def count_bad_values(grid, solution):
    eq_values = np.logical_and(True, grid == solution)
    print("size array : ", len(grid)**2)
    return len(grid)**2 - np.count_nonzero(eq_values)


def manhattan_dist(x1, y1, x2, y2):
    # print("x1 : " + str(x1) + " / " + "x2 : " + str(x2) + " / " + "y1 : " + str(y1) + " / " + "y2 : " + str(y2))
    # print("abs(x2 - x1) : ", abs(x2 - x1))
    # print("abs(y2 - y1) : ", abs(y2 - y1))
    # print("res : ", abs(x2 - x1) + abs(y2 - y1))
    return abs(x2 - x1) + abs(y2 - y1)


def sq_euclidian_dist(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


def uniform(x1, y1, x2, y2):
    return 0


def calc_heuristic(function, size, puzzle, solution):
    if puzzle.parent is None:
        h_sum = 0
        for x in range(0, size*size):
            point1 = np.where(puzzle.state == x)
            point2 = np.where(solution == x)
            h_sum += function(point1[0][0], point1[1][0], point2[0][0], point2[1][0])
        # print("h_sum all : ", h_sum)

    else:
        #
        # print("other node")
        # print("puzzle.parent.state :")
        # print(puzzle.parent.state)
        # print("state : ")
        # print(puzzle.state)
        h_sum = puzzle.parent.h
        # print("h_sum parent : ", h_sum)
        solution_zero = np.where(solution == 0)
        solution_value = np.where(solution == puzzle.parent.state[puzzle.zero_position[0],
                                                                         puzzle.zero_position[1]])
        parent_zero = np.where(puzzle.parent.state == 0)
        value = [parent_zero[0], parent_zero[1]]
        # print("value : ", value)
        # print(parent_zero)

        # print(parent_zero)

        parent_value = np.where(puzzle.parent.state == puzzle.state[value[0], value[1]])

        curr_zero = np.where(puzzle.state == 0)
        #
        # print("puzzle.state[puzzle.parent.zero_position] :",
        #       puzzle.state[parent_zero[0], parent_zero[1]])
        # print("parent_value : ", parent_value)

        curr_value = np.where(puzzle.state == puzzle.state[value[0], value[1]])

        # print("curr value where : x == ", puzzle.state[value[0], value[1]])
        # print("curr_value : ", curr_value)


        h_sum -= function(parent_zero[0][0], parent_zero[1][0], solution_zero[0][0], solution_zero[1][0])
        # print("h_sum - h zero : ", h_sum)
        h_sum -= function(parent_value[0][0], parent_value[1][0], solution_value[0][0], solution_value[1][0])
        # print("h_sum - parent value : ", h_sum)

        h_sum += function(curr_zero[0][0], curr_zero[1][0], solution_zero[0][0], solution_zero[1][0])
        # print("h_sum + curr 0 : ", h_sum)

        # print("curr_value : ", curr_value)
        # print("solution_value : ", solution_value)

        h_sum += function(curr_value[0][0], curr_value[1][0], solution_value[0][0], solution_value[1][0])
        # print("h_sum + curr val : ", h_sum)

        # print("h_sum apres : ", h_sum)
    # if np.array_equal(puzzle.state, np.array([[2 ,8 ,3],[1 ,5 ,6],[0, 7, 4]])):
    #     exit()
    return h_sum


def get_heuristic(heuristic_number):
    heuristic_list = [manhattan_dist, sq_euclidian_dist, count_bad_values, uniform]
    return heuristic_list[int(heuristic_number) - 1]
