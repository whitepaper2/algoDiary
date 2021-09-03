#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 下午2:21
# @Author  : pengyuan.li
# @Site    : 
# @File    : 062_unique_paths.py
# @Software: PyCharm


def unique_paths(m, n):
    """
    note: 大问题拆分为子问题，矩阵表示与常规正好相反
    动态规划，机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    path = [[1] * m] * n
    for i in range(1, n):
        for j in range(1, m):
            path[i][j] = path[i - 1][j] + path[i][j - 1]
    return path[n - 1][m - 1]


def unique_paths3(m, n):
    """
    note: 大问题拆分为子问题，矩阵表示与常规正好相反
    动态规划，机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i-1, j-1)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    处理边缘值，dp[0][1]=1 or dp[1][0]=1，其他值初始化=0
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    path = [[0] * (m + 1) for _ in range(n + 1)]
    path[0][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            path[i][j] = path[i - 1][j] + path[i][j - 1]
    return path[n][m]


def unique_paths2(m, n):
    """
    note: 大问题拆分为子问题，节省空间，保存一维数据（不太明白？？？），每行保存一个值，更新方式：d[i] = d[i] + d[i-1]
    动态规划，机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    path = [1] * n
    for j in range(1, m):
        for i in range(1, n):
            path[i] = path[i - 1] + path[i]
    return path[n - 1]


def unique_paths4(m, n):
    """
    note: 大问题拆分为子问题，经典递归问题。从下到上
    机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """

    def sub_paths(cur_i, cur_j, m, n):
        if cur_i > m or cur_j > n:
            return 0
        if cur_i == m and cur_j == n:
            return 1
        return sub_paths(cur_i + 1, cur_j, m, n) + sub_paths(cur_i, cur_j + 1, m, n)

    return sub_paths(1, 1, m, n)


def unique_paths5(m, n):
    """
    note: 大问题拆分为子问题，经典递归问题。从上到下
    机器人只能向右或向下移动，dp[i][j]表示从左上角到坐标(i, j)的路径长度，状态转移公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """

    def sub_paths(cur_i, cur_j, m, n):
        if cur_i < 0 or cur_j < 0:
            return 0
        if cur_i == 0 or cur_j == 0:
            return 1
        return sub_paths(cur_i - 1, cur_j, m, n) + sub_paths(cur_i, cur_j - 1, m, n)

    return sub_paths(m - 1, n - 1, m, n)


def unique_paths6(m, n):
    """
    note: 排列组合问题。机器人向下走m-1步，向右走n-1步，这些步数组合得到最后结果。C(m+n,m) = A(m+n,m)/A(m,m)
    :type m: int，列数
    :type n: int，行数
    :rtype: int，不同路径的个数
    """
    small = min(m,n)-1
    big = max(m,n)-1
    p = 1
    q = 1
    for i in range(1, small+1):
        p = p * i
        q = q * ((small + big) + 1 - i)

    return q//p


if __name__ == "__main__":
    m = 7
    n = 3
    print(unique_paths(1, 1))
    print(unique_paths3(m, n))
    print(unique_paths4(m, n))
    print(unique_paths5(m, n))
    print(unique_paths6(m, n))
