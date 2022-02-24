#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/02/11 14:15:53
@Author  : pengyuan.li
@File    : 4.3.3-lca.py
@Software: VSCode
'''

# here put the import lib
from collections import defaultdict
import math
'''
求有根无向图两节点的公共父节点，与二叉树求公共父节点还是不同的。
'''


def lca(relations, root, u, v):
    """
    向上标记法
    @param relations:图的边关系
    @param root:根节点
    @param u,v:待查询两节点
    @return : 
    """
    adj = defaultdict(list)
    vertex = set()

    def _init():
        for p, q in relations:
            adj[p].append(q)
            adj[q].append(p)
            vertex.add(p)
            vertex.add(q)

    _init()

    parent = dict()
    depth = dict()
    visited = {p: 0 for p in vertex}

    def _dfs(node, nodeParent, nodeDepth):
        parent[node] = nodeParent
        depth[node] = nodeDepth
        visited[node] = 1
        for p in adj[node]:
            if visited[p] == 0:
                _dfs(p, node, nodeDepth + 1)

    _dfs(root, -1, 0)

    while depth[u] > depth[v]:
        u = parent[u]
    while depth[u] < depth[v]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]

    return u


def lca2(relations, root, u, v):
    """
    树上倍增法，使用二维数组存储，dp[x][k] = dp[dp[x,k-1],k-1]，表示从x开始向上走2^k步到达的父节点，因此节点转换为整数
    @param relations:图的边关系
    @param root:根节点
    @param u,v:待查询两节点
    @return : 
    """
    adj = defaultdict(list)
    vertex = set()

    def _init():
        for p, q in relations:
            adj[p].append(q)
            adj[q].append(p)
            vertex.add(p)
            vertex.add(q)

    _init()

    n = len(vertex)
    t = int(math.log2(n)) + 1
    parent = [[0 for _ in range(n + 1)] for _ in range(t + 1)]
    depth = [0] * (n + 1)
    visited = [0] * (n + 1)

    def _dfs(node, nodeParent, nodeDepth):
        parent[0][node] = nodeParent
        depth[node] = nodeDepth
        visited[node] = 1
        for p in adj[node]:
            if visited[p] == 0:
                _dfs(p, node, nodeDepth + 1)

    _dfs(root, -1, 0)

    for i in range(t):
        for j in range(1, n + 1):
            if parent[i][j] < 0:
                parent[i + 1][j] = -1
            else:
                parent[i + 1][j] = parent[i][parent[i][j]]

    if depth[u] > depth[v]:
        u, v = v, u
    for k in range(t + 1):
        if (depth[v] - depth[u]) >> k & 1:
            v = parent[k][v]
    if u == v:
        return u
    for k in range(t, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]


if __name__ == "__main__":
    relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [5, 7], [5, 8]]
    root = 1
    u, v = 5, 6
    print(lca2(relations, root, u, v))

    u, v = 5, 2
    print(lca2(relations, root, u, v))
