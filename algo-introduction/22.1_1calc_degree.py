#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 下午7:35
# @Author  : pengyuan.li
# @Site    : 
# @File    : 22.1_1calc_degree.py
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


def calcIndegree(G):
    indegree = defaultdict(int)
    for u, vs in G.adj.items():
        indegree[u] += 0
        for v in vs:
            indegree[v] += 1
    return dict(indegree)


def calcOutdegree(G):
    outdegree = dict()
    for u, vs in G.adj.items():
        outdegree[u] = len(vs)
    return outdegree


def transposeGraph(G):
    vertex = G.vertex
    edge = []
    for u, vs in G.adj.items():
        for v in vs:
            edge.append([v, u])
    return DirectionGraph(vertex, edge)


def delReplEdge(G):
    vertex = G.vertex
    edge = []
    for u, vs in G.adj.items():
        for v in list(set(vs)):
            if v != u:
                edge.append([u, v])
    return DirectionGraph(vertex, edge)


if __name__ == "__main__":
    # 有向图
    vertex = [1, 2, 3, 4, 5, 6]
    edge = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    graph = DirectionGraph(vertex, edge)
    # graph = DirectionGraph.createGraphByEdge(edge)
    print(graph.adj)
    print(calcOutdegree(graph))
    print(calcIndegree(graph))
    graph2 = transposeGraph(graph)
    print(graph2.adj)
    graph3 = delReplEdge(graph)
    print(graph3.adj)
    # 无向图
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    edge = [['r', 's'], ['r', 'v'], ['s', 'w'], ['w', 't'], ['w', 'x'], ['x', 'u'], ['x', 'y'], ['u', 'y']]
    # graph = UnDirectionGraph(vertex, edge)
    graph = UnDirectionGraph.createGraphByEdge(edge)
