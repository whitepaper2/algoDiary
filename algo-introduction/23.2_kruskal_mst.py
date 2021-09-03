#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

from collections import defaultdict


class UnDirectionGraph(object):
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
            self.adj[v].append((u, w))

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


class UnionSet(object):
    def __init__(self, sets):
        self.rank = dict()
        self.parent = dict()
        self.setsNum = len(sets)
        for s in sets:
            self.rank[s] = 1
            self.parent[s] = s

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xHead = self.find(x)
        yHead = self.find(y)
        if xHead == yHead:
            return
        xHRank = self.rank[xHead]
        yHRank = self.rank[yHead]
        if xHRank > yHRank:
            self.parent[yHead] = xHead
        else:
            if xHRank == yHRank:
                self.rank[yHead] += 1
            self.parent[xHead] = yHead


def kruskalMst(G):
    """
    kruskal生成无向权重图的最小生成树
    :param G:
    :return: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
    """
    ust = UnionSet(G.vertex)
    edges = G.edge
    nonDescEdges = sorted(edges, key=lambda x: x[2])
    # print(nonDescEdges)
    mst = list()
    for u, v, w in nonDescEdges:
        if ust.find(u) != ust.find(v):
            ust.union(u, v)
            mst.append((u, v, w))
    return mst


if __name__ == "__main__":
    # 无向图
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edge = [['a', 'b', 4], ['a', 'h', 8], ['b', 'h', 11], ['b', 'c', 8], ['c', 'i', 2], ['h', 'i', 7], ['h', 'g', 1],
            ['c', 'f', 4], ['i', 'g', 6], ['g', 'f', 2], ['d', 'c', 7], ['d', 'f', 14], ['f', 'e', 10], ['d', 'e', 9]]
    graph = UnDirectionGraph(vertex, edge)
    # print(graph.adj)
    print(kruskalMst(graph))
