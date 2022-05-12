#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/05/11 20:14:21
@Author  : pengyuan.li
@File    : 0x21-reacheable.py
@Software: VSCode
'''

# here put the import lib

from collections import defaultdict, deque
from typing import List
from bitarray import bitarray


def reacheable(edges: List[List[int]]) -> List[int]:
    """
    edges:有向无环图
    寻找每个点可以到达的个数，c[x] = {x}U{c[y1],c[y2]...}，x->y1, x->y2
    """
    adj = defaultdict(list)
    indegree = defaultdict(int)
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
        indegree[u] += 0
    pq = deque()
    for k, v in indegree.items():
        if v == 0:
            pq.append(k)
    seq = []
    while pq:
        t = pq.popleft()
        seq.append(t)
        for u in adj[t]:
            indegree[u] -= 1
            if indegree[u] == 0:
                pq.append(u)
    N = 11
    f = [bitarray('0' * N) for _ in range(N)]
    for i in range(len(seq) - 1, -1, -1):
        x = seq[i]
        f[x][x] = 1
        for u in adj[x]:
            f[x] |= f[u]
    res = []
    for i in range(1, N):
        res.append(max(f[i].count(), 1))
    return res


if __name__ == "__main__":
    edges = [[3, 8], [2, 3], [2, 5], [5, 9], [5, 9], [2, 3], [3, 9], [4, 8],
             [2, 10], [4, 9]]
    print(reacheable(edges))