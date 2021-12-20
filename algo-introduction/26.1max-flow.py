#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 下午4:35
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.1max-flow.py
# @Software: PyCharm

# 最大流最小切割算法

from collections import deque
from copy import deepcopy
from datetime import datetime


class DirectionGraph(object):
    def __init__(self, vertex, edge):
        parallelEdge = self._checkParallelEdge(edge)
        if parallelEdge:
            for u, v, w in parallelEdge:
                v2 = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
                vertex.append(v2)
                edge.remove([u, v, w])
                edge.append([u, v2, w])
                edge.append([v2, v, w])
        self.ROW = len(vertex)
        self.vertex2idx = dict()
        self.idx2vertex = dict()
        for i, v in enumerate(vertex):
            self.vertex2idx[v] = i
            self.idx2vertex[i] = v
        self.graph = [[0] * self.ROW for _ in range(self.ROW)]
        for u, v, w in edge:
            self.graph[self.vertex2idx[u]][self.vertex2idx[v]] = w
        self.rawGraph = deepcopy(self.graph)

    def _checkParallelEdge(self, edge):
        uniEdge = set()
        parallelEdge = list()
        for u, v, w in edge:
            if '|'.join(sorted([u, v])) not in uniEdge:
                uniEdge.add('|'.join(sorted([u, v])))
            else:
                parallelEdge.append([u, v, w])
        return parallelEdge

    def _searchPathByBFS(self, s, t, parent):
        """
        是否存在从s->t的路径
        :param s: 源点
        :param t: 终点
        :param parent:存储经过的路径
        :return: bool
        """
        visited = [False] * self.ROW
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            cur = queue.popleft()
            for idx, cap in enumerate(self.graph[cur]):
                if not visited[idx] and cap > 0:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = cur
        return True if visited[t] else False

    def fordFulkerson(self, source, sink):
        """
        计算最大流有2种方法：
        1、fordFulkerson是一种方法，有不同实现方式寻找增广路径，本程序使用bfs
        2、推送-重贴标签（也叫预流推进算法）
        返回最大流
        :param source: 源点
        :param sink: 终点
        :return:
        """
        maxFlow = 0
        parent = [-1] * self.ROW
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]
        while self._searchPathByBFS(source, sink, parent):
            pathFlow = float('inf')
            s = sink
            while s != source:
                pathFlow = min(pathFlow, self.graph[parent[s]][s])
                s = parent[s]
            maxFlow += pathFlow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= pathFlow
                self.graph[v][u] -= pathFlow
                v = parent[v]
        return maxFlow

    def printPathByBFS(self, source):
        s = self.vertex2idx[source]
        flowGraph = list()
        print(self.graph)
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

    def pushRelabel(self, source, sink):
        """
        计算最大流有2种方法：
        1、fordFulkerson是一种方法，有不同实现方式寻找增广路径，本程序使用bfs
        2、推送-重贴标签（也叫预流推进算法）
        返回最大流
        :param source: 源点
        :param sink: 终点
        :return:
        """
        # 1.init
        flow = [0] * self.ROW
        height = [0] * self.ROW
        edgeFlow = self.graph
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]
        height[source] = self.ROW
        for v, w in enumerate(self.graph[source]):
            if w:
                edgeFlow[source][v] -= w
                edgeFlow[v][source] += w
                flow[v] += w
                flow[source] -= w

        def _check():
            for i in range(self.ROW):
                if flow[i] > 0 and i != sink:
                    return True
            return False

        def _push(x):
            flag = False
            for i in range(self.ROW):
                if edgeFlow[x][i] and height[x] == height[i] + 1:
                    delta = min(flow[x], edgeFlow[x][i])
                    edgeFlow[x][i] -= delta
                    edgeFlow[i][x] += delta
                    flow[x] -= delta
                    flow[i] += delta
                    flag = True
            return flag

        def _change(x):
            res = float('inf')
            for i in range(self.ROW):
                if edgeFlow[x][i] > 0:
                    res = min(res, height[i])
            if res == float('inf'):
                res -= 1
            height[x] = res + 1
            return

        while _check():
            for i in range(self.ROW):
                if flow[i] > 0:
                    if not _push(i):
                        _change(i)
                        height[sink] = 0
        return flow[sink]


if __name__ == "__main__":
    # 1.单向图，矩阵表示
    vertex = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    edge = [['s', 'v1', 16], ['s', 'v2', 13], ['v1', 'v3', 12], ['v2', 'v1', 4], ['v2', 'v4', 14], ['v3', 'v2', 9],
            ['v3', 't', 20], ['v4', 'v3', 7], ['v4', 't', 4]]
    g = DirectionGraph(vertex, edge)
    source = 's'
    sink = 't'
    maxFlow = g.pushRelabel(source, sink)
    print("maxFlow={}".format(maxFlow))
    # 1.单向图，矩阵表示
    vertex = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    edge = [['s', 'v1', 16], ['s', 'v2', 13], ['v1', 'v3', 12], ['v2', 'v1', 4], ['v2', 'v4', 14], ['v3', 'v2', 9],
            ['v3', 't', 20], ['v4', 'v3', 7], ['v4', 't', 4]]
    g = DirectionGraph(vertex, edge)
    source = 's'
    sink = 't'
    maxFlow = g.fordFulkerson(source, sink)
    print("maxFlow={}".format(maxFlow))
    print(g.printPathByBFS(source))
    # todo:形成环或双向边
    vertex = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    edge = [['s', 'v1', 16], ['s', 'v2', 13], ['v1', 'v3', 12], ['v2', 'v1', 4], ['v2', 'v4', 14], ['v3', 'v2', 9],
            ['v3', 't', 20], ['v4', 'v3', 7], ['v4', 't', 4], ['v1', 'v2', 10], ['v3', 'v4', 20]]
    g = DirectionGraph(vertex, edge)
    source = 's'
    sink = 't'
    maxFlow = g.fordFulkerson(source, sink)
    print("maxFlow={}".format(maxFlow))
    print(g.printPathByBFS(source))
