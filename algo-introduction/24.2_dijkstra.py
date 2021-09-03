#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

import heapq
from collections import defaultdict


class DirectionGraph(object):
    def __init__(self, vertex, edge):
        """
        :param vertex: [u1,u2,...]
        :param edge: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
        """
        self.vertex = vertex
        self.adj = defaultdict(list)
        self.edge = edge
        for u, v, w in edge:
            self.adj[u].append((v, w))

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


def initialSingleSource(G, s):
    """
    初始化图中各节点的上界、父节点
    :param G:
    :param s:
    :return:
    """
    maxDist, parent = dict(), dict()
    for u in G.vertex:
        maxDist[u] = float("inf")
        parent[u] = None
    maxDist[s] = 0
    return maxDist, parent


def relax(u, v, w, maxDist, parent):
    if maxDist[v] > maxDist[u] + w:
        maxDist[v] = maxDist[u] + w
        parent[v] = u

from queue import PriorityQueue
from pyspark.sql import Window
def dijkstra(G, s):
    """
    dijkstra计算单源最短路径问题，权重非负，返回路径
    :param G:
    :return: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
    """
    maxDist, parent = initialSingleSource(G, s)
    minHeap = [(w, u) for u, w in maxDist.items()]
    heapq.heapify(minHeap)
    paths = []
    while minHeap:
        wu, u = heapq.heappop(minHeap)
        paths.append(u)
        for v, wv in G.adj[u]:
            relax(u, v, wv, maxDist, parent)
        minHeap = [(w, u) for u, w in maxDist.items() if u not in paths]
        heapq.heapify(minHeap)
    print(maxDist)
    return paths


if __name__ == "__main__":
    # 有向图
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edge = [['a', 'b', 4], ['a', 'h', 8], ['b', 'h', 11], ['b', 'c', 8], ['c', 'i', 2], ['h', 'i', 7], ['h', 'g', 1],
            ['c', 'f', 4], ['i', 'g', 6], ['g', 'f', 2], ['d', 'c', 7], ['d', 'f', 14], ['f', 'e', 10], ['d', 'e', 9]]
    graph = DirectionGraph(vertex, edge)
    # print(graph.adj)
    print(dijkstra(graph, 'a'))

    # 有向图
    vertex = ['s', 't', 'x', 'y', 'z']
    edge = [['s', 't', 10], ['t', 'x', 1], ['t', 'y', 2], ['s', 'y', 5], ['y', 'z', 2], ['y', 'x', 9], ['x', 'z', 4],
            ['z', 'x', 6], ['y', 't', 3], ['z', 's', 7]]
    graph = DirectionGraph(vertex, edge)
    # print(graph.adj)
    print(dijkstra(graph, 's'))
