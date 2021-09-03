#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

from collections import defaultdict


class DirectionGraph:
    def __init__(self, vertex, edge):

        self.vertex = vertex
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
    finished = dfs(G)
    return sorted(finished.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    # graph = DirectionGraph(vertex, edge)
    graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(dfs(graph))
    print(topoSort(graph))
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'], ['x', 'u'], ['x', 'y'], ['u', 'y']]
