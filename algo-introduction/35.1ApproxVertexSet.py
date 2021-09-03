#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

import copy
import heapq
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
        for u, v in edge:
            self.adj[u].append(v)
            self.adj[v].append(u)


def approxVertexSets(G):
    """
    贪心算法，返回最小规模的顶点覆盖，近似算法代价 <= 2*最优算法代价
    :param G:
    :return:
    """
    C = []
    for u, v in G.edge:
        if u not in C and v not in C:
            C.append(u)
            C.append(v)
    return C


def approxVertexSets2(G):
    """
    返回最小规模的顶点覆盖，最大顶点匹配解法
    :param G:
    :return:
    """
    C = []
    E = copy.copy(G.edge)
    while E:
        u, v = E[0]
        C.extend([u, v])
        E.remove([u, v])
        for v2 in G.adj[u]:
            if [u, v2] in E:
                E.remove([u, v2])
            if [v2, u] in E:
                E.remove([v2, u])
        for u2 in G.adj[v]:
            if [v, u2] in E:
                E.remove([v, u2])
            if [u2, v] in E:
                E.remove([u2, v])
    return C


def approxVertexSets3(G):
    """
    贪心算法，返回最小规模的顶点覆盖，近似算法代价 <= 2*最优算法代价
    按照最大度选择顶点，删除相邻边
    :param G:
    :return:
    """
    C = []
    E = copy.copy(G.edge)
    while E:
        numDict = defaultdict(list)
        for u, v in E:
            numDict[u].append(v)
            numDict[v].append(u)
        numTup = []
        for k, v in numDict.items():
            numTup.append((-len(v), k))
        heapq.heapify(numTup)
        n, topVertex = heapq.heappop(numTup)
        C.append(topVertex)
        for v2 in G.adj[topVertex]:
            if [topVertex, v2] in E:
                E.remove([topVertex, v2])
            if [v2, topVertex] in E:
                E.remove([v2, topVertex])
    return C


if __name__ == "__main__":
    # 无向图
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edge = [['a', 'b'], ['b', 'c'], ['c', 'e'], ['c', 'd'], ['d', 'e'], ['d', 'f'], ['d', 'g'], ['e', 'f']]
    graph = UnDirectionGraph(vertex, edge)
    print(approxVertexSets(graph))
    print(approxVertexSets2(graph))
    print(approxVertexSets3(graph))
