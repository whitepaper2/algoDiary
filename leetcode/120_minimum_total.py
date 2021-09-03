#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 下午9:58
# @Author  : pengyuan.li
# @Site    : 
# @File    : 120_minimum_total.py
# @Software: PyCharm


def minimum_total(triangle):
    """
    note: 相邻节点（三角形中的），动态规划，可以看成是自底向上的，中间过程使用二维数组保存数据
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = []
    for i in range(len(triangle) + 1):
        dp.append([0] * (i + 1))
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(i + 1):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
    return dp[0][0]


def minimum_total2(triangle):
    """
    note: 相邻节点（三角形中的），动态规划，可以看成是自底向上的，中间过程使用一维数组保存数据，节约存储空间
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * (len(triangle) + 1)
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]


def minimum_total3(triangle):
    """
    note: 相邻节点（三角形中的），动态规划，可以看成是自底向上的，中间过程使用一维数组保存数据，少一次判断，节省大量时间
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = triangle[len(triangle) - 1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(len(triangle))
    print(minimum_total(triangle))
    print(minimum_total2(triangle))
    print(minimum_total3(triangle))
