#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 下午5:34
# @Author  : pengyuan.li
# @Site    : 
# @File    : 073_setZeros.py
# @Software: PyCharm

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    note:首先找出所有0值的横、纵下标，然后再遍历这些下标对原数据进行替换
    """
    m = len(matrix)
    n = len(matrix[0])
    row0 = set()
    col0 = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row0.add(i)
                col0.add(j)
    for ele in row0:
        matrix[ele] = [0] * n
    for i in range(m):
        for ele in col0:
            matrix[i][ele] = 0


def setZeroes2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    note:1.查找第一行、第一列是否存在0；2.除第一行、第一列，如果有0，修改第一行、第一列对应的值为0；
    3.遍历除第一行、第一列以外的元素，如果对应的第一行、第一列有0值，则修改为0；4.修改第一行、第一列
    """
    m = len(matrix)
    n = len(matrix[0])
    isrowzero = False
    iscolzero = False
    for i in range(n):
        if matrix[0][i] == 0:
            isrowzero = True
    for i in range(m):
        if matrix[i][0] == 0:
            iscolzero = True
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if isrowzero:
        for i in range(n):
            matrix[0][i] = 0
    if iscolzero:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes2(matrix)
    print(matrix)

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes2(matrix)
    print(matrix)
