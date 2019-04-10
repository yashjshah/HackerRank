#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass_sum(matrix, r, c):
    return matrix[r + 0][c + 0] + matrix[r + 0][c + 1] + matrix[r + 0][c + 2] \
                                + matrix[r + 1][c + 1] + \
           matrix[r + 2][c + 0] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]

def max_hourglass_sum(matrix):

    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return None

    max_sum = -sys.maxsize - 1
    for r in range(0, len(matrix) - 2):
        for c in range(0, len(matrix[0]) - 2):
            current_sum = hourglass_sum(matrix, r, c)
            max_sum = max(current_sum, max_sum)
    return max_sum

def main():
    matrix = []
    for _ in range(0, 6):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(max_hourglass_sum(matrix))

if __name__ == "__main__":
    main()

