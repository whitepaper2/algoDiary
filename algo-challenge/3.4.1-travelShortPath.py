#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 下午5:38
# @Author  : pengyuan.li
# @Site    :
# @File    : 3.4.1-travelShortPath.py
# @Software: PyCharm


def tsp(neighbors):
    """
    :param neighbors:
    :return:
    """
    n = len(neighbors)
    dp = [[-1 for _ in range(n)] for _ in range(1 << n)]

    def rec(S, v):
        """
        :param S: 已访问过的集合
        :param v: 当前节点
        :return:
        """
        if dp[S][v] >= 0:
            return dp[S][v]
        if S == (1 << n) - 1 and v == 0:
            dp[S][v] = 0
            return dp[S][v]
        res = float('inf')
        for u in range(n):
            if not S >> u & 1:
                res = min(res, rec(S | 1 << u, u) + neighbors[v][u])
        dp[S][v] = res
        return dp[S][v]

    return rec(0, 0)


def tsp2(neighbors):
    """
    :param neighbors:
    :return:
    """
    n = len(neighbors)
    dp = [[float('inf') for _ in range(n)] for _ in range(1 << n)]
    dp[(1 << n) - 1][0] = 0
    for S in range((1 << n) - 2, -1, -1):
        for v in range(n):
            for u in range(n):
                if not S >> u & 1:
                    dp[S][v] = min(dp[S][v],
                                   dp[S | 1 << u][u] + neighbors[v][u])
    return dp[0][0]


def weightTsp(neighbors, t, a, b):
    """
    
    Arguments
    ---------
    neighbors:邻接矩阵,表示道路间的长度
    t:车票
    a,b:起始点、终点
    Returns
    -------
    float，道路间长度除以车票数
    """
    n = len(t)
    m = len(neighbors)
    dp = [[float('inf')] * m for _ in range(1 << n)]
    print(dp)
    dp[(1 << n) - 1][a - 1] = 0
    res = float('inf')
    for S in range((1 << n) - 1, -1, -1):
        res = min(res, dp[S][b - 1])
        for v in range(m):
            for i in range(n):
                if S >> i & 1:
                    for u in range(m):
                        if neighbors[v][u] >= 0:
                            dp[S & ~(1 << i)][u] = min(
                                dp[S & ~(1 << i)][u],
                                dp[S][v] + neighbors[v][u] / t[i])
    return res


if __name__ == "__main__":
    # 邻接矩阵如下，其中1000：无穷大或无连接；初始值：默认0
    neighbors = [[1000, 3, 1000, 4, 1000], [1000, 1000, 5, 1000, 1000],
                 [4, 1000, 1000, 5, 1000], [1000, 1000, 1000, 1000, 3],
                 [7, 6, 1000, 1000, 1000]]
    print(tsp(neighbors))
    print(tsp2(neighbors))

    # 带权值的旅行商问题
    neighbors = [[1000, 1000, 3, 2], [1000, 1000, 3, 5], [3, 3, 1000, 1000],
                 [2, 5, 1000, 1000]]
    tickets = [3, 1]
    a, b = 2, 1  # 起始点、终点
    print(weightTsp(neighbors, tickets, a, b))
