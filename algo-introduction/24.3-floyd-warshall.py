#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 下午5:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 24.3-floyd-warshall.py
# @Software: PyCharm


"""
求任意两点间的距离
"""
from collections import defaultdict


class DirectionGraph(object):
    def __init__(self, vertex, edge):
        """

        :param vertex: [u1,u2,...]
        :param edge: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
        """
        self.n = len(vertex)
        self.vertex2id = {}
        self.id2vertex = {}
        for i, e in enumerate(vertex):
            self.vertex2id[e] = i
            self.id2vertex[i] = e

        self.adj = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.adj[i][i] = 0
        for u, v, w in edge:
            idx = self.vertex2id[u]
            idy = self.vertex2id[v]
            self.adj[idx][idy] = w


def floydWarshall(graph):
    n = graph.n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph.adj[i][j] = min(graph.adj[i][j], graph.adj[i][k] + graph.adj[k][j])
    return graph.adj


if __name__ == "__main__":
    # 有向图
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edge = [['a', 'b', 4], ['a', 'h', 8], ['b', 'h', 11], ['b', 'c', 8], ['c', 'i', 2], ['h', 'i', 7], ['h', 'g', 1],
            ['c', 'f', 4], ['i', 'g', 6], ['g', 'f', 2], ['d', 'c', 7], ['d', 'f', 14], ['f', 'e', 10], ['d', 'e', 9]]
    graph = DirectionGraph(vertex, edge)
    # print(graph.adj)
    print(floydWarshall(graph))
