#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    :
# @File    : 21.1_union_sets.py
# @Software: PyCharm

from collections import defaultdict, deque


class DirectionGraph:

    def __init__(self, vertex, edge):

        self.vertex = vertex
        self.edge = edge
        self.adj = defaultdict(list)
        for u, v in edge:
            self.adj[u].append(v)

    @classmethod
    def createGraphByEdge(cls, edge):
        tmp = []
        for u, v in edge:
            tmp.extend([u, v])
        vertex = list(set(tmp))
        return cls(vertex, edge)


def dfs(G):
    color, parent, discovered, finished = dict(), dict(), dict(), dict()
    WHITE, GRAY, BLACK = 0, 1, 2
    time = 0
    for u in G.vertex:
        color[u] = WHITE
        parent[u] = None

    def subDfs(G, s):
        nonlocal time
        time += 1
        discovered[s] = time
        color[s] = GRAY
        for u in G.adj[s]:
            if color[u] == WHITE:
                parent[u] = s
                subDfs(G, u)
        color[s] = BLACK
        time += 1
        finished[s] = time

    for u in G.vertex:
        if color[u] == WHITE:
            subDfs(G, u)
    return finished


def topoSort(G):
    # 深度优先遍历
    finished = dfs(G)
    return sorted(finished.items(), key=lambda x: -x[1])


def topoSort2(G):
    # 通过顶点的入度计算，不断寻找入度为0的顶点
    pq = deque()
    vertex = G.vertex
    edge = G.edge
    adj = G.adj
    indegree = {x: 0 for x in vertex}
    for u, v in edge:
        indegree[v] += 1
    for k, v in indegree.items():
        if v == 0:
            pq.append(k)
    res = []
    while pq:
        t = pq.popleft()
        res.append(t)
        for u in adj[t]:
            # res.append(u)
            indegree[u] -= 1
            if indegree[u] == 0:
                pq.append(u)
    if len(res) != len(vertex):
        print("无法完成拓扑排序！")
    else:
        print(res)


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    # graph = DirectionGraph(vertex, edge)
    graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(dfs(graph))
    print(topoSort(graph))
    print(topoSort2(graph))
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'],
            ['x', 'u'], ['x', 'y'], ['u', 'y']]
