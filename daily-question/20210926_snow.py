#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 下午3:11
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20210926_snow.py
# @Software: PyCharm


def getMaxPath(grid):
    """
    第260场周赛，网格游戏
    """
    c = len(grid[0])

    left = 0
    right = 0
    for i in range(1, c):
        right += grid[0][i]
    maxPath = right
    for i in range(1, c):
        left += grid[1][i - 1]
        right -= grid[0][i]
        maxPath = min(maxPath, max(left, right))
    return maxPath


def printPos(a, b):
    """
    计算偏移，约瑟夫环，《算法进阶》hash，判断6边型是否相等。
    :param a:
    :param b:
    :return:
    """
    n = len(a)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(a[(i + k) % n], b[(j + k) % n])


if __name__ == "__main__":
    grid = [[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]]
    print(getMaxPath(grid))

    a = [1, 2, 3, 4, 5, 6]
    b = [2, 3, 4, 5, 6, 1]
    printPos(a, b)
   