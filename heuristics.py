import numpy as np

puzzle = np.array([[2, 4, 6, 1],
    [3, 7, 8, 10],
    [0, 5, 15, 12],
    [9, 11, 13, 14]])
solution = np.array([[2, 4, 6, 5],
    [3, 7, 8, 12],
    [0, 13, 15, 10],
    [9, 1, 11, 14]])

def count_good_values(grid, solution):
    eq_values = np.logical_and(True, grid == solution)
    count = np.count_nonzero(eq_values)
    print (eq_values)
    print(count)
    return count  count_good_values(puzzle, solution)
