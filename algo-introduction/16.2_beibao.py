#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def beibao01(weights, values, maxWeight):
    """
    note:0-1背包问题,dp[i][j]，前i个物品在容量为j的情况下的最大价值
    dp[i][j] = dp[i-1][j], weights[i]>j
    dp[i][j] = max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i]), weights[i]<j
    :param weights: 物品重量
    :param values: 物品价值
    :param maxWeight: 背包可容纳的最大重量
    :return: 最大价值
    """
    m = len(weights)
    dp = [[0] * (maxWeight + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, maxWeight + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    return dp[m][maxWeight]


def recursiveFirstFinish(startTimes, finishTimes):
    """
    note:迭代求解
    :param startTimes: 开始时间
    :param finishTimes: 结束时间（默认递增）
    :return: 活动的下标
    """
    n = len(startTimes)

    def subRecursive(startTimes, finishTimes, curi, n):
        m = curi + 1
        while m < n and startTimes[m] < finishTimes[curi]:
            m += 1
        if m < n:
            return [m] + subRecursive(startTimes, finishTimes, m, n)
        else:
            return []

    return subRecursive(startTimes, finishTimes, 0, n)


if __name__ == "__main__":
    w = [2, 3, 4, 5, 9]
    v = [3, 4, 5, 8, 10]
    maxW = 20
    print(beibao01(w, v, maxW))
