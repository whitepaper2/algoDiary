#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午5:31
# @Author  : pengyuan.li
# @Site    : 
# @File    : 059_generateMatrix.py
# @Software: PyCharm
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    """
    note:使用指针记录遍历规则，top->right->bottom->left
    :param n:
    :return:
    """
    out = [[0 for _ in range(n)] for _ in range(n)]
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    side = 0
    res = 1
    while left <= right and top <= bottom:
        # top
        if side == 0:
            i = top
            for j in range(left, right + 1):
                out[i][j] = res
                res = res + 1
            top = top + 1
        # right
        if side == 1:
            j = right
            for i in range(top, bottom + 1):
                out[i][j] = res
                res = res + 1
            right = right - 1
        # bottom
        if side == 2:
            i = bottom
            for j in range(right, left - 1, -1):
                out[i][j] = res
                res = res + 1
            bottom = bottom - 1
        # left
        if side == 3:
            j = left
            for i in range(bottom, top - 1, -1):
                out[i][j] = res
                res = res + 1
            left = left + 1
        side = (side + 1) % 4
    return out


if __name__ == "__main__":
    n = 3
    print(generateMatrix(n))
    print(generateMatrix(4))
