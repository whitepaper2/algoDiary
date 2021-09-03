#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 下午3:05
# @Author  : pengyuan.li
# @Site    : 
# @File    : 054_spiral_order.py
# @Software: PyCharm

# 顺时针访问矩阵
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1
    result = []
    side = 0
    while top <= bottom and left <= right:
        if side == 0:
            i = top
            for j in range(left, right + 1):
                result.append(matrix[i][j])
            top = top + 1
        if side == 1:
            j = right
            for i in range(top, bottom + 1):
                result.append(matrix[i][j])
            right = right - 1
        if side == 2:
            i = bottom
            for j in range(right, left - 1, -1):
                result.append(matrix[i][j])
            bottom = bottom - 1
        if side == 3:
            j = left
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][j])
            left = left + 1
        side = (side + 1) % 4
    return result


def spiral_order2(matrix: List[List[int]]) -> List[int]:
    """
    note：计算环数，遍历矩阵
    :param matrix:
    :return:
    """
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    out = []
    p = m
    q = n
    c = (min(m, n) + 1) // 2
    for i in range(c):
        for col in range(i, i + q):
            out.append(matrix[i][col])
        for row in range(i + 1, i + p):
            out.append(matrix[row][i + q - 1])
        if p == 1 or q == 1:
            break
        for col in range(i + q - 2, i - 1, -1):
            out.append(matrix[i + p - 1][col])
        for row in range(i + p - 2, i, -1):
            out.append(matrix[row][i])
        p = p - 2
        q = q - 2
    return out


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral_order(matrix))
    print(spiral_order2(matrix))
