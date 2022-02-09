#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/02/08 10:31:35
@Author  : pengyuan.li
@File    : 4.3.1-strongConnectComponent.py
@Software: VSCode
'''

# here put the import lib
from collections import defaultdict


def ssc(n, edges):
    used = [0] * (n + 1)
    adj = defaultdict(list)
    radj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    vertex = []

    def dfs(u):
        used[u] = 1
        for v in adj[u]:
            if used[v] == 0:
                dfs(v)
        vertex.append(u)

    dfs(12)
    cmps = [0] * (n + 1)
    used = [0] * (n + 1)

    def rdfs(u, k):
        used[u] = 1
        cmps[u] = k
        for v in radj[u]:
            if used[v] == 0:
                rdfs(v, k)

    k = 0
    for u in vertex:
        if used[u] == 0:
            k += 1
            rdfs(u, k)
    return k


if __name__ == "__main__":
    n = 12
    edges = [[12, 11], [11, 8], [11, 10], [8, 10], [10, 9], [9, 8], [9, 7],
             [7, 6], [6, 5], [5, 7], [6, 3], [6, 4], [4, 3], [4, 1], [2, 3],
             [3, 2]]
    print(ssc(n, edges))
