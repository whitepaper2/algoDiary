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


if __name__ == "__main__":
    neighbors = [[1000, 3, 1000, 4, 1000], [1000, 1000, 5, 1000, 1000], [4, 1000, 1000, 5, 1000],
                 [1000, 1000, 1000, 1000, 3], [7, 6, 1000, 1000, 1000]]
    print(tsp(neighbors))
