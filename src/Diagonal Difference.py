#!/bin/python3

arr_multiple_v2 = [
    [6, 6, 7, -10, 9, -3, 8, 9, -1],
    [9, 7, -10, 6, 4, 1, 6, 1, 1],
    [-1, -2, 4, -6, 1, -4, -6, 3, 9],
    [-8, 7, 6, -1, -6, -6, 6, -7, 2],
    [-10, -4, 9, 1, -7, 8, -5, 3, -5],
    [-8, -3, -4, 2, -3, 7, -5, 1, -5],
    [-2, -7, -4, 8, 3, -1, 8, 2, 3],
    [-3, 4, 6, -7, -7, -8, -3, 9, -6],
    [-2, 0, 5, 4, 4, 4, -3, 3, 0],
]


"""
Final method to sum the diagonal numbers from the array 
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""


def diagonal_difference_multiple_v2(__getitem__):
    """
    Passed 11 test
    :param __getitem__:
    :return:
    """
    sum_a = 0
    sum_b = 0
    for index, array in enumerate(__getitem__):
        sum_a = sum_a + array[index]

    for index, array in enumerate(__getitem__):
        list_reversed = list(reversed(array))
        sum_b = sum_b + list_reversed[index]

    print("sum_a => ", sum_a)
    print("sum_b => ", sum_b)
    if sum_a > sum_b:
        print(sum_a - sum_b)
    else:
        print(sum_b - sum_a)
    print(sum_a - sum_b)
