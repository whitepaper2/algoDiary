#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 下午4:51
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.5.3-graphColor.py
# @Software: PyCharm

from typing import List
from collections import defaultdict
import heapq


def graphColor(n: int, relation: List[List[int]]) -> str:
    """
    n个节点构成的图，能否使用2中颜色找色
    :param n:
    :param relation:
    :return:
    """
    neighbors = defaultdict(list)
    for x, y in relation:
        neighbors[x].append(y)
        neighbors[y].append(x)
    color = [0] * n

    def _dfs(v, c):
        color[v] = c
        for u in neighbors[v]:
            if color[u] == c:
                return False
            if color[u] == 0 and not _dfs(u, -c):
                return False
        return True

    for i in range(n):
        if color[i] == 0:
            if not _dfs(i, 1):
                return 'No'
    return 'Yes'


def secondMinPath(N, edges):
    """
    求顶点1-N的次短路径长度
    minPath[v] = minPath[u]+dist(u,v)
    secondMinPath[v] = secondMinPath[u]+dist(u,v) or minPath[u]+dist(u,v)
    :param N: 顶点个数
    :param edges:
    :return:
    """
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    minDist = [float('inf')] * (N + 1)
    secondMinDist = [float('inf')] * (N + 1)
    minDist[1] = 0
    minHeap = [(0, 1)]
    heapq.heapify(minHeap)
    while minHeap:
        td, t = heapq.heappop(minHeap)
        if secondMinDist[t] < td:
            continue
        for v, w in adj[t]:
            curdist = td + w
            if minDist[v] > curdist:
                minDist[v], curdist = curdist, minDist[v]
                heapq.heappush(minHeap, (minDist[v], v))
            if minDist[v] < curdist < secondMinDist[v]:
                secondMinDist[v] = curdist
                heapq.heappush(minHeap, (secondMinDist[v], v))
    print(secondMinDist)
    return secondMinDist[N]


if __name__ == "__main__":
    edges = [[0, 1], [0, 3], [1, 2], [2, 3]]
    print(graphColor(4, edges))

    edges = [[1, 2, 100], [2, 3, 250], [2, 4, 200], [3, 4, 100]]
    print(secondMinPath(4, edges))
