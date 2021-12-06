#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 上午9:30
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.4.2-gasStation.py
# @Software: PyCharm

import heapq
from typing import List


def gasStation(L: int, P: int, A: List[int], B: List[int]) -> int:
    """
    每经过的加油站，在后面的过程中都可以使用
    :param L: 行驶里程
    :param P: 初始油箱油量
    :param A: 加油站位置
    :param B: 加油站可加油量
    :return:
    """
    A.append(L)
    B.append(0)
    priorQueue = []
    heapq.heapify(priorQueue)
    res = 0
    gas = P
    curPos = 0
    for i, a in enumerate(A):
        d = a - curPos
        while gas - d < 0:
            if not priorQueue:
                return -1
            t = -heapq.heappop(priorQueue)
            gas += t
            res += 1
        gas -= d
        curPos = a
        heapq.heappush(priorQueue, -B[i])

    return res


def foodChain(N: int, queries: List[List[int]]) -> int:
    """
    返回矛盾信息
    :param N:
    :param queries:
    :return:
    """
    parent = [0] * (3 * N + 1)
    rank = [0] * (3 * N + 1)

    def init(n):
        for i in range(n):
            parent[i] = i
            rank[i] = 0

    def find(x):
        if x == parent[x]:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def unite(x, y):
        px = find(x)
        py = find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            parent[px] = py
        else:
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] = rank[py] + 1

    def issame(x, y):
        return find(x) == find(y)

    res = 0
    init(3 * N)
    for qtype, x, y in queries:
        x, y = x - 1, y - 1
        if x < 0 or x >= N or y < 0 or y >= N:
            res += 1
            continue
        if qtype == 'First':
            if issame(x, y + N) or issame(x, y + 2 * N):
                res += 1
            else:
                unite(x, y)
                unite(x + N, y + N)
                unite(x + 2 * N, y + 2 * N)
        else:
            if issame(x, y) or issame(x, y + 2 * N):
                res += 1
            else:
                unite(x, y + N)
                unite(x + N, y + 2 * N)
                unite(x + 2 * N, y)

    return res


if __name__ == "__main__":
    L = 25
    P = 10
    A = [10, 14, 20, 21]
    B = [10, 5, 2, 4]
    print(gasStation(L, P, A, B))

    N = 100
    queries = [['First', 101, 1], ['Second', 1, 2], ['Second', 2, 3], ['Second', 3, 3], ['First', 1, 3],
               ['Second', 3, 1], ['First', 5, 5]]
    print(foodChain(N, queries))
