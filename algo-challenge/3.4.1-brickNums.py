#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 下午3:31
# @Author  : pengyuan.li
# @Site    : 
# @File    : 3.4.1-brickNums.py
# @Software: PyCharm

from typing import List


def brickNums(color: List[List[int]]) -> int:
    """
    现有1*2的砖头，能得到多少种摆放方式
    :param color: T/F, T黑色，不可铺砖
    :return:
    """
    rows, cols = len(color), len(color[0])
    used = [[0 for _ in range(cols)] for _ in range(rows)]
    print(rows, cols, used)

    def rec(i, j, used):
        """
        :param i:
        :param j:
        :param used:
        :return:
        """
        if j == cols:
            return rec(i + 1, 0, used)
        if i == rows:
            # 覆盖所有空格？只能横着放
            return 1
        if used[i][j] or color[i][j]:
            return rec(i, j + 1, used)
        res = 0
        used[i][j] = 1
        # 1.横着放
        if j + 1 < cols and not used[i][j + 1] and not color[i][j + 1]:
            used[i][j + 1] = 1
            res += rec(i, j + 1, used)
            used[i][j + 1] = 0
        # 2.竖着放
        if i + 1 < rows and not used[i + 1][j] and not color[i + 1][j]:
            used[i + 1][j] = 1
            res += rec(i, j + 1, used)
            used[i + 1][j] = 0
        used[i][j] = 0
        return res

    return rec(0, 0, used)


def brickNums2(color: List[List[int]]) -> int:
    """
    现有1*2的砖头，能得到多少种摆放方式
    :param color: T/F, T黑色，不可铺砖
    :return:
    """
    rows, cols = len(color), len(color[0])
    dp0, dp1 = [0] * (1 << cols), [0] * (1 << cols)
    dp0[0] = 1
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            for used in range(1 << cols):
                if used >> j & 1 or color[i][j]:
                    dp1[used] = dp0[used & ~(1 << j)]
                else:
                    res = 0
                    if j + 1 < cols and not (used >> (j + 1) & 1) and not color[i][j + 1]:
                        res += dp0[used | 1 << (j + 1)]
                    if i + 1 < rows and not color[i + 1][j]:
                        res += dp0[used | 1 << j]
                    dp1[used] = res
            dp0, dp1 = dp1, dp0
    return dp0[0]


if __name__ == "__main__":
    color = [[False, False, False], [False, True, False], [False, False, False]]
    print(color)
    print(brickNums(color))
    print(brickNums2(color))
