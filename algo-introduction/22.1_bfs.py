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


class DirectionWeightGraph:
    def __init__(self, vertex, edge):
        """
        :param vertex: list表示[u1,u2,u3]
        :param edge: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
        """
        self.vertex = vertex
        self.adj = defaultdict(list)
        for u, v, w in edge:
            self.adj[u].append((v, w))

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


def bfs(G, s):
    if s not in G.vertex:
        print("源点 %s 不在图中，无法求距离".format(s))
        return
    WHITE, GRAY, BLACK = 0, 1, 2
    color, dist, parent = dict(), dict(), dict()
    for u in G.vertex:
        color[u] = WHITE
        dist[u] = float("inf")
        parent[u] = None
    color[s] = GRAY
    dist[s] = 0
    parent[s] = None
    queue = deque()
    queue.append(s)
    while queue:
        head = queue.popleft()
        for v in G.adj[head]:
            if color[v] == WHITE:
                color[v] = GRAY
                dist[v] = dist[head] + 1
                parent[v] = head
                queue.append(v)
        color[head] = BLACK
    return dist


def bfs2(G, s):
    """
    结点是否被访问过，单字节表示
    :param G:
    :param s: 源节点
    :return:
    """
    if s not in G.vertex:
        print("源节点{}不在图中".format(s))
    WHITE, GRAY = 0, 1
    color, parent, dist = dict(), dict(), dict()
    for u in G.vertex:
        color[u] = WHITE
        parent[u] = None
        dist[u] = float("inf")
    color[s] = GRAY
    dist[s] = 0
    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        for v in G.adj[u]:
            if color[v] == WHITE:
                color[v] = GRAY
                parent[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist, parent


def printPath(parent, s, v):
    """

    :param parent: 广度优先搜索树
    :param s: 源节点
    :param v: 目标节点
    :return:
    """
    if s == v:
        print(s)
    elif parent[v] is None:
        print("{}->{}没有路径".format(s, v))
        return
    else:
        print("{}->".format(v))
        printPath(parent, s, parent[v])


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    graph = DirectionGraph(vertex, edge)
    # graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(bfs(graph, 3))
    dist, parent = bfs2(graph, 3)
    print(parent)
    printPath(parent, 3, 4)
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2, 3], [1, 4, 1], [4, 2, 2], [2, 5, 4], [5, 4, 10], [3, 5, 5], [3, 6, 3], [6, 6, 2]]
    wgraph = DirectionWeightGraph(vertex, edge)
    print(wgraph.adj)
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'], ['x', 'u'], ['x', 'y'], ['u', 'y']]
    # graph = UnDirectionGraph(vertex, edge)
    graph = UnDirectionGraph.createGraphByEdge(edge)
    print(bfs(graph, 's'))
