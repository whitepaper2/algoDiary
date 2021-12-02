#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 下午3:07
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.3.1-knapsack.py
# @Software: PyCharm

from typing import List


def knapsack01(w: List[int], v: List[int], maxW: int) -> int:
    """
    有n个物品(重量w,价值v)，挑选出不超过重量maxW的物品的最大价值。
    1<n<100,1<maxW<10000，可分离物品重量和价值作为2维矩阵。
    若两者范围更大，则会超时
    :param w:
    :param v:
    :param maxW:
    :return:
    """
    n = len(w)
    dp = [[0 for _ in range(maxW + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, maxW + 1):
            if j < w[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
    return dp[n][maxW]


def knapsack01Bydfs(w: List[int], v: List[int], maxW: int) -> int:
    """
    有n个物品(重量w,价值v)，挑选出不超过重量maxW的物品的最大价值。
    1<n<100,1<maxW<10000，可分离物品重量和价值作为2维矩阵。
    若两者范围更大，则会超时
    :param w:
    :param v:
    :param maxW:
    :return:
    """
    n = len(w)

    def dfs(i, j):
        """
        从第i个点开始挑选重量不超过j的物品的最大价值
        :param i:
        :param j:
        :return:
        """
        if i == n:
            res = 0
        elif w[i] > j:
            res = dfs(i + 1, j)
        else:
            res = max(dfs(i + 1, j), dfs(i + 1, j - w[i]) + v[i])
        return res

    return dfs(0, maxW)


def knapsack01Bydfsmemo(w: List[int], v: List[int], maxW: int) -> int:
    """
    有n个物品(重量w,价值v)，挑选出不超过重量maxW的物品的最大价值。
    1<n<100,1<maxW<10000，可分离物品重量和价值作为2维矩阵。
    若两者范围更大，则会超时
    备忘录法
    :param w:
    :param v:
    :param maxW:
    :return:
    """
    n = len(w)
    memo = [[-1 for _ in range(maxW + 1)] for _ in range(n + 1)]

    def dfs(i, j):
        """
        从第i个点开始挑选重量不超过j的物品的最大价值
        :param i:
        :param j:
        :return:
        """
        if memo[i][j] >= 0:
            return memo[i][j]
        if i == n:
            res = 0
        elif w[i] > j:
            res = dfs(i + 1, j)
        else:
            res = max(dfs(i + 1, j), dfs(i + 1, j - w[i]) + v[i])
        memo[i][j] = res
        return res

    return dfs(0, maxW)


if __name__ == "__main__":
    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    maxW = 5
    print(knapsack01(w, v, maxW))
    print(knapsack01Bydfs(w, v, maxW))
    print(knapsack01Bydfsmemo(w, v, maxW))
