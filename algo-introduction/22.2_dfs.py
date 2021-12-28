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


class UnDirectionGraph(object):

    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.adj = defaultdict(list)
        for u, v in edge:
            self.adj[u].append(v)
            self.adj[v].append(u)

    @classmethod
    def createGraphByEdge(cls, edge):
        """
        note: 可实现多态性，先调用该方法处理原始数据=>标准输入，再调用构造函数
        :param edge:
        :return:
        """
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
    return parent, discovered, finished


def dfs2(G):
    """
    1位表示是否被访问过
    :param G:
    :return:
    """
    color, parent, discovered, finished = dict(), dict(), dict(), dict()
    WHITE, GRAY = 0, 1
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
        time += 1
        finished[s] = time

    for u in G.vertex:
        if color[u] == WHITE:
            subDfs(G, u)
    return parent, discovered, finished


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    # graph = DirectionGraph(vertex, edge)
    graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(dfs(graph))
    print(dfs2(graph))
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'],
            ['x', 'u'], ['x', 'y'], ['u', 'y']]
    # graph = UnDirectionGraph(vertex, edge)
    graph = UnDirectionGraph.createGraphByEdge(edge)
