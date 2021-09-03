#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 下午1:51
# @Author  : pengyuan.li
# @Site    : 
# @File    : 048_rotate.py
# @Software: PyCharm
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    note:90度旋转矩阵，可以先交换第一列和最后一列，然后沿对角线对折交换数值
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if i != j:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
    for x in matrix:
        x.reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
