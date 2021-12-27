#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 下午8:06
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.1-weightMaxFlow.py
# @Software: PyCharm


"""
最小费用最大流问题，在取得最大流的基础上，求最小费用
流量为F时费用的最小值。
解决方法：在残余网络中寻找最小费用（bellman-ford,spfa,dijkstra）
"""

from collections import deque
from copy import deepcopy
from datetime import datetime


class DirectionGraph(object):
    def __init__(self, vertex, edge):
        parallelEdge = self._checkParallelEdge(edge)
        if parallelEdge:
            for u, v, w, c in parallelEdge:
                v2 = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
                vertex.append(v2)
                edge.remove([u, v, w, c])
                edge.append([u, v2, w, c])
                edge.append([v2, v, w, c])
        self.ROW = len(vertex)
        self.vertex2idx = dict()
        self.idx2vertex = dict()
        for i, v in enumerate(vertex):
            self.vertex2idx[v] = i
            self.idx2vertex[i] = v
        self.graph = [[0] * self.ROW for _ in range(self.ROW)]
        self.cost = [[0] * self.ROW for _ in range(self.ROW)]
        for u, v, w, c in edge:
            self.graph[self.vertex2idx[u]][self.vertex2idx[v]] = w
            self.cost[self.vertex2idx[u]][self.vertex2idx[v]] = c
        self.rawGraph = deepcopy(self.graph)

    def _checkParallelEdge(self, edge):
        uniEdge = set()
        parallelEdge = list()
        for u, v, w, c in edge:
            if '|'.join(sorted([u, v])) not in uniEdge:
                uniEdge.add('|'.join(sorted([u, v])))
            else:
                parallelEdge.append([u, v, w, c])
        return parallelEdge

    def minCostByspfa(self, source, sink):
        """
        :param source: 源点
        :param sink: 终点
        :return:
        """
        maxFlow = 0
        minCost = 0
        parent = [-1] * self.ROW
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]
        nodeCost = [float('inf')] * self.ROW

        def _spfa(s, t, parent):
            """
            :param s:
            :param t:
            :return:
            """
            nonlocal nodeCost
            nodeCost = [float('inf')] * self.ROW
            visited = [0] * self.ROW
            queue = deque()
            queue.append(s)
            visited[s] = 1
            nodeCost[s] = 0
            while queue:
                t = queue.popleft()
                for v, w in enumerate(self.graph[t]):
                    if w > 0 and nodeCost[v] > nodeCost[t] + self.cost[t][v]:
                        nodeCost[v] = nodeCost[t] + self.cost[t][v]
                        parent[v] = t
                        if not visited[v]:
                            visited[v] = 1
                            queue.append(v)
            print(nodeCost, parent)
            return parent[t] != -1

        def _bellmanFord(s, t, parent):
            nonlocal nodeCost
            nodeCost = [float('inf')] * self.ROW
            nodeCost[s] = 0
            update = True
            while update:
                update = False
                for i in range(self.ROW):
                    if nodeCost[i] == float('inf'):
                        continue
                    for v, w in enumerate(self.graph[i]):
                        if w > 0 and nodeCost[v] > nodeCost[i] + self.cost[i][v]:
                            nodeCost[v] = nodeCost[i] + self.cost[i][v]
                            parent[v] = i
                            update = True
            return nodeCost[t] != float('inf')

        while _spfa(source, sink, parent):
            # while _bellmanFord(source, sink, parent):
            pathFlow = float('inf')
            s = sink
            while s != source:
                pathFlow = min(pathFlow, self.graph[parent[s]][s])
                s = parent[s]
            maxFlow += pathFlow
            minCost += pathFlow * nodeCost[sink]
            print(minCost)
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= pathFlow
                self.graph[v][u] += pathFlow
                v = parent[v]
        return maxFlow, minCost

    def printPathByBFS(self, source):
        s = self.vertex2idx[source]
        flowGraph = list()
        for g1, g2 in zip(self.rawGraph, self.graph):
            cur = list()
            for c1, c2 in zip(g1, g2):
                if c2 >= 0:
                    cur.append(c1 - c2)
                else:
                    cur.append(0)
            flowGraph.append(cur)
        queue = deque()
        queue.append(s)
        path = dict()
        while queue:
            cur = queue.popleft()
            for idx, cap in enumerate(flowGraph[cur]):
                if cap > 0:
                    path[(self.idx2vertex[cur], self.idx2vertex[idx])] = cap
                    queue.append(idx)
        return path


if __name__ == "__main__":
    # 1.单向图，矩阵表示，spfa算法
    vertex = ['s', 'v1', 'v2', 'v3', 't']
    edge = [['s', 'v3', 10, 5], ['v3', 'v1', 12, 5], ['v1', 't', 10, 15], ['s', 't', 10, 10],
            ['v3', 't', 5, 10]]
    g = DirectionGraph(vertex, edge)
    source = 's'
    sink = 't'
    maxFlow = g.minCostByspfa(source, sink)
    print("maxFlow={}".format(maxFlow))
