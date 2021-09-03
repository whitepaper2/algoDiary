#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 下午2:21
# @Author  : pengyuan.li
# @Site    : 
# @File    : 062_unique_paths.py
# @Software: PyCharm

from typing import List


def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
    """
    note: 大问题拆分为子问题，矩阵表示与常规正好相反
    动态规划，机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])
    if obstacleGrid is None or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
        return 0
    path = [[0] * (m + 1) for _ in range(n + 1)]
    path[0][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if obstacleGrid[i - 1][j - 1] != 0:
                continue
            path[i][j] = path[i - 1][j] + path[i][j - 1]
    return path[n][m]


def unique_paths_with_obstacles2(obstacleGrid: List[List[int]]) -> int:
    """
    note: 大问题拆分为子问题，节省空间，保存一维数据（不太明白？？？），每行保存一个值，更新方式：d[i] = d[i] + d[i-1]
    动态规划，机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid is None or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
        return 0
    path = [0] * n
    path[0] = 1
    for i in range(0, m):
        for j in range(0, n):
            if obstacleGrid[i][j] == 1:
                path[j] = 0
            elif j > 0:
                path[j] = path[j - 1] + path[j]
    return path[n - 1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]
                    ]
    print(unique_paths_with_obstacles(obstacleGrid))
    print(unique_paths_with_obstacles2(obstacleGrid))
