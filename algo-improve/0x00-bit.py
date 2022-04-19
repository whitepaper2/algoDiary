#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/19 11:20:09
@Author  : pengyuan.li
@File    : 0x00-bit.py
@Software: VSCode
'''


# here put the import lib
# 位运算，求 a^b mod p
def mypow(a, b, p):
    """
    b表示为二进制，递推公式 a^(2^k)=(a^(2^(k-1)))^2
    """
    res = 1 % p
    while b > 0:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b = b >> 1
    return res


def isHamiltonPath(n, graph, path):
    """
    n:顶点个数
    graph:邻接矩阵
    path:一条路径
    return:是否是哈密尔顿回路，True or False 
    note: path = n+1个顶点 and 每个点都走到 and 首尾相连 
    """
    # 下标从1开始
    visited = [0] * (n + 1)
    if len(path) != n + 1:
        return False
    pathLen = len(path)
    if path[0] != path[pathLen - 1]:
        return False
    for i in range(pathLen - 1):
        if not graph[path[i]][path[i + 1]]:
            return False
        visited[path[i]] = 1
    for i in range(1, n + 1):
        if not visited[i]:
            return False
    return True


def minHamiltonPath(n, graph):
    """
    n:顶点个数
    graph:邻接矩阵
    return:求顶点0——n-1的哈密尔顿最短路径
    """
    dp = [[float('inf')] * n for _ in range(1 << n)]

    dp[1][0] = 0
    for i in range(1, 1 << n):
        for j in range(n):
            # 经过的点的集合i，当前点位置j，只计算j在集合i的路径
            if i >> j & 1:
                for k in range(n):
                    # k在集合1^(1<<j)
                    if (i ^ (1 << j)) >> k & 1:
                        dp[i][j] = min(dp[i][j],
                                       dp[i ^ (1 << j)][k] + graph[k][j])

    return dp[(1 << n) - 1][n - 1]


# 起床困难综合征，通过一系列的位运算使得结果最大，求初始值x
def boss(m, doors):
    """
    m:数据的取值范围，[0,m]
    doors:['or',d]
    """
    n = len(doors)
    N = 15

    def calc(bit, now):
        for q, v in doors:
            x = v >> bit & 1
            if q == "AND":
                now &= x
            elif q == "OR":
                now |= x
            elif q == "XOR":
                now ^= x
            else:
                print("error")
        return now

    cur = 0
    res = 0
    for i in range(N, -1, -1):
        res0 = calc(i, 0)
        res1 = calc(i, 1)
        if cur + (1 << i) <= m and res0 < res1:
            cur += (1 << i)
            res += (res1 << i)
        else:
            res += (res0 << i)
    return res


if __name__ == "__main__":
    a = 3
    b = 10
    p = 10000000007
    print(mypow(a, b, p))

    n = 6
    edges = [[6, 2, 1], [3, 4, 2], [1, 5, 3], [2, 5, 2], [3, 1, 1], [4, 1, 3],
             [1, 6, 2], [6, 3, 3], [1, 2, 4], [4, 5, 2]]
    graph = [[float('inf')] * n for _ in range(n)]
    for u, v, w in edges:
        graph[u - 1][v - 1] = w
        graph[v - 1][u - 1] = w
    print(minHamiltonPath(n, graph))

    n = 6
    edges = [[6, 2, 1], [3, 4, 2], [1, 5, 3], [2, 5, 2], [3, 1, 1], [4, 1, 3],
             [1, 6, 2], [6, 3, 3], [1, 2, 4], [4, 5, 2]]
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    # path = [5, 1, 4, 3, 6, 2, 5]
    path = [6, 1, 2, 5, 4, 3, 1]
    print(isHamiltonPath(
        n,
        graph,
        path,
    ))

    m = 10
    doors = [['AND', 5], ['OR', 6], ['XOR', 7]]
    print(boss(m, doors))
