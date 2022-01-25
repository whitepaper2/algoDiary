#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/25 16:18:55
@Author  : pengyuan.li
@File    : 4.1.1-gaussJordan.py
@Software: VSCode
'''

# here put the import lib

from typing import List


def gaussJordan(A: List[List[int]], b: List[int]):
    """
    解n个未知量，n个方程
    """
    n = len(A)
    B = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]
        B[i][n] = b[i]

    for i in range(n):
        pivoti = i
        for j in range(i + 1, n):
            if abs(B[j][i]) > abs(B[pivoti][i]):
                pivoti = j
        B[i], B[pivoti] = B[pivoti], B[i]
        for j in range(n, i - 1, -1):
            B[i][j] = B[i][j] / B[i][i]
        for k in range(n):
            if i != k:
                for j in range(n, i - 1, -1):
                    B[k][j] -= B[k][i] * B[i][j]

    print(B)
    res = [B[i][-1] for i in range(n)]
    return res


if __name__ == "__main__":
    A = [[1, -2, 3], [4, -5, 6], [7, -8, 10]]
    b = [6, 12, 21]
    print(gaussJordan(A, b))
