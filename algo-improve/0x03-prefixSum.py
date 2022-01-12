#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/11 17:45:13
@Author  : pengyuan.li
@File    : 0x03-prefixSum.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def maxBomb(A: List[List[int]], r: int) -> int:
    """
    一颗炸弹在区域r内能获得最大价值
    :param: A:List[List[int]]
    :param: r:int
    :return:
    """
    m, n = len(A), len(A[0])
    preSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            preSum[i + 1][j + 1] = preSum[i + 1][j] + preSum[i][
                j + 1] - preSum[i][j] + A[i][j]
    res = 0
    for i in range(m):
        for j in range(n):
            leftx, lefty = max(1, i - r + 1), max(1, j - r + 1)
            res = max(
                res, preSum[i + 1][j + 1] - preSum[i + 1][lefty] -
                preSum[leftx][j + 1] + preSum[leftx][lefty])
    return res


if __name__ == "__main__":
    mat = [[0, 0, 1], [1, 1, 1]]
    r = 1
    print(maxBomb(mat, r))
