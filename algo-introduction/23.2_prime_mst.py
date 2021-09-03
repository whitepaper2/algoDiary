#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

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


# 如何构建支持reduce-key的优先级队列？解决该问题
def primeMst(G, s):
    """
    prime生成无向权重图的最小生成树
    :param G:
    :return: [[u1,v1,w1],[u2,v2,w2],[u3,v3,w3]]
    """
    weight, parent = dict(), dict()
    for u in G.vertex:
        weight[u] = float("inf")
        parent[u] = None
    weight[s] = 0
    minHeap = [(weight[u], u) for u in G.vertex]
    heapq.heapify(minHeap)
    mst = list()
    while minHeap:
        uw, u = heapq.heappop(minHeap)
        mst.append(u)
        for v, vw in G.adj[u]:
            curVertex = [x[1] for x in minHeap]
            if v in curVertex and vw < weight[v]:
                weight[v] = vw
                parent[v] = u
            # 1.decrease weight,O(n)
            minHeap = [(weight[u], u) for u in curVertex]
            heapq.heapify(minHeap)
            # 2.decrease weight, 0(lgN), siftup
    return mst, parent


if __name__ == "__main__":
    # 无向图
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edge = [['a', 'b', 4], ['a', 'h', 8], ['b', 'h', 11], ['b', 'c', 8], ['c', 'i', 2], ['h', 'i', 7], ['h', 'g', 1],
            ['c', 'f', 4], ['i', 'g', 6], ['g', 'f', 2], ['d', 'c', 7], ['d', 'f', 14], ['f', 'e', 10], ['d', 'e', 9]]
    graph = UnDirectionGraph(vertex, edge)
    # print(graph.adj)
    print(primeMst(graph, 'a'))
