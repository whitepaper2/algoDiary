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


def knapsack01Complete(w: List[int], v: List[int], maxW: int) -> int:
    """
    物品类别(重量w,价值v)，可以使用无数次，挑选出不超过重量maxW的物品的最大价值。
    1<n<100,1<maxW<10000，可分离物品重量和价值作为2维矩阵。
    若两者范围更大，则会超时
    :param w:
    :param v:
    :param maxW:
    :return:
    """
    n = len(w)
    dp = [[0 for _ in range(maxW + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(maxW + 1):
            if j < w[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])
    print(dp)
    return dp[n][maxW]


def knapsack01_2(w: List[int], v: List[int], maxW: int) -> int:
    """
    有n个物品(重量w,价值v)，挑选出不超过重量maxW的物品的最大价值。
    1<n<100, 1<maxW<10^9, 1<w[i]<10^7, 1<v[i]<100
    根据物品重量和价值取值范围，重量较大，可分离出价值
    dp[i+1][j]: 前i个物品中价值和j的最小重量
    :param w:
    :param v:
    :param maxW:
    :return:
    """
    n = len(w)
    maxV = sum(v)
    dp = [[float('inf') for _ in range(maxV + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(maxV + 1):
            if j < v[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
    res = 0
    for i in range(maxV + 1):
        if dp[n][i] <= maxW:
            res = i
    return res


def knapsack02(a: List[int], m: List[int], K: int) -> bool:
    """
    多重部分和问题。即多重背包问题
    现有数组，n个数值(数值a,个数v)，判断是否能构成和恰为K的子数组。
    1<n<100, 1<a[i], m[i]<10^5, 1<K<10^5
    dp[i+1][j]: 前i个数构成和j
    :param a:
    :param m:
    :param K:
    :return:
    """
    n = len(a)
    dp = [[False for _ in range(K + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(K + 1):
            if j < a[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                for k in range(m[i] + 1):
                    if j - k * a[i] >= 0:
                        dp[i + 1][j] |= dp[i][j - k * a[i]]
    print(dp)
    return dp[n][K]


def knapsack02_2(a: List[int], m: List[int], K: int) -> bool:
    """
    多重部分和问题。即多重背包问题
    现有数组，n个数值(数值a,个数v)，判断是否能构成和恰为K的子数组。
    1<n<100, 1<a[i], m[i]<10^5, 1<K<10^5
    dp[i+1][j]: 前i个数构成和j
    减少复杂度
    :param a:
    :param m:
    :param K:
    :return:
    """
    n = len(a)
    # 1.method 1
    # dp = [[-1 for _ in range(K + 1)] for _ in range(n + 1)]
    # dp[0][0] = 0
    # for i in range(n):
    #     for j in range(K + 1):
    #         if dp[i][j] >= 0:
    #             dp[i + 1][j] = m[i]
    #         elif j < a[i] or dp[i + 1][j - a[i]] <= 0:
    #             dp[i + 1][j] = -1
    #         else:
    #             dp[i + 1][j] = dp[i + 1][j - a[i]] - 1
    #
    # print(dp)
    # return dp[n][K] >= 0
    # 2.method 2
    dp = [-1 for _ in range(K + 1)]
    dp[0] = 0
    for i in range(n):
        for j in range(K + 1):
            if dp[j] >= 0:
                dp[j] = m[i]
            elif j < a[i] or dp[j - a[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j - a[i]] - 1
    return dp[K] >= 0


if __name__ == "__main__":
    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    maxW = 5
    print(knapsack01(w, v, maxW))
    print(knapsack01Bydfs(w, v, maxW))
    print(knapsack01Bydfsmemo(w, v, maxW))

    w = [3, 4, 2]
    v = [4, 5, 3]
    maxW = 7
    print(knapsack01Complete(w, v, maxW))

    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    maxW = 5
    print(knapsack01_2(w, v, maxW))

    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    print(knapsack02(a, m, K))

    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    print(knapsack02_2(a, m, K))
