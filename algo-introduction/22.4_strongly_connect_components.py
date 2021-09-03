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


def transportGraph(G):
    vertex = G.vertex
    edge = []
    for u in G.adj:
        for v in G.adj[u]:
            edge.append([v, u])
    return DirectionGraph(vertex, edge)


def dfs(G, vertics=None):
    color, parent, discovered, finished = dict(), dict(), dict(), dict()
    WHITE, GRAY, BLACK = 0, 1, 2
    time = 0
    connects = list()
    for u in G.vertex:
        color[u] = WHITE
        parent[u] = None

    def subDfs(G, s, cur):
        nonlocal time
        time += 1
        discovered[s] = time
        color[s] = GRAY
        for u in G.adj[s]:
            if color[u] == WHITE:
                parent[u] = s
                cur.append(u)
                subDfs(G, u, cur)
        color[s] = BLACK
        time += 1
        finished[s] = time
    vvs = vertics if vertics is not None else G.vertex
    for u in vvs:
        if color[u] == WHITE:
            cur = [u]
            subDfs(G, u, cur)
            connects.append(cur)
    return finished, connects


def stronglyConnectComponents(G):
    finished, connects = dfs(G)
    vertex = [x[0] for x in sorted(finished.items(), key=lambda x: -x[1])]
    print(vertex)
    graph2 = transportGraph(G)
    return dfs(graph2, vertex)


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    # graph = DirectionGraph(vertex, edge)
    graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(dfs(graph))
    print(stronglyConnectComponents(graph))
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'], ['x', 'u'], ['x', 'y'], ['u', 'y']]
