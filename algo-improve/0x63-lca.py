#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 下午4:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x63-lca.py
# @Software: PyCharm


"""
两节点的最近公共祖先
"""
from collections import defaultdict, deque
import math


def getLCAByIncreament(outEdges, queries):
    """
    倍增法
    :param outEdges:
    :param queries:
    :return:
    """
    adj = defaultdict(list)
    vertices = set()
    for u, v in outEdges:
        adj[u].append(v)
        vertices.add(u)
        vertices.add(v)
    n = len(vertices)
    t = int(math.log2(n)) + 1
    f = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    depth = [0] * (n + 1)
    dist = [0] * (n + 1)

    def bfs(adj, u):
        """
        :param adj:邻接表
        :param u: 源点
        :return:
        """
        queue = deque()
        queue.append(u)
        depth[u] = 1
        while queue:
            v = queue.popleft()
            for p in adj[v]:
                if visited[p]:
                    continue
                queue.append(p)
                visited[p] = 1
                depth[p] = depth[v] + 1
                dist[p] = dist[v] + 1  # 可改为边的权重
                f[p][0] = v
                for j in range(1, t + 1):
                    f[p][j] = f[f[p][j - 1]][j - 1]

    def lca(x, y):
        if depth[x] > depth[y]:
            x, y = y, x
        for i in range(t, -1, -1):
            if depth[f[y][i]] >= depth[x]:
                y = f[y][i]
        if x == y:
            return x
        for i in range(t, -1, -1):
            if f[x][i] != f[y][i]:
                x = f[x][i]
                y = f[y][i]
        return f[x][0]

    bfs(adj, 1)
    print(f)
    for x, y in queries:
        c = lca(x, y)
        print('*' * 50)
        print('common-ancessor={}'.format(c))
        print('dist({},{})={}'.format(x, y, dist[x] + dist[y] - 2 * dist[c]))


if __name__ == "__main__":
    """
    有根树，根节点是1
    """
    outEdges = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [4, 7], [4, 8], [7, 9]]
    queries = [[7, 2], [6, 9], [1, 2], [9, 8], [7, 9]]
    getLCAByIncreament(outEdges, queries)
