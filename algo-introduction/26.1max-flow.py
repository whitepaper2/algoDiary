#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 下午4:35
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.1max-flow.py
# @Software: PyCharm

"""
求网络中最大流问题, 有两种方法：
1、增广路
  代表实现方法如下：
  1.1fordFulkerson，最大流+dfs
  1.2Edmonds–Karp算法(简称:EK)，最大流+bfs，避免某些输入数据通过dfs寻找超时问题
  1.3Dinic算法，早于EK发明算法，之后引入bfs层次图概念优化

2、重贴标签（2.1通用方法；2.2前置重贴标签）
"""

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

    def edmondsKarp(self, source, sink):
        """
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
                self.graph[v][u] += pathFlow
                v = parent[v]
        return maxFlow

    def dinic(self, source, sink):
        maxFlow = 0
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]
        level = [0] * self.ROW

        def dinicBFS():
            queue = deque()
            nonlocal level
            level = [-1] * self.ROW
            level[source] = 0
            queue.append(source)
            while queue:
                u = queue.popleft()
                for v, w in enumerate(self.graph[u]):
                    if level[v] < 0 and w:
                        level[v] = level[u] + 1
                        queue.append(v)
            return level[sink] > 0

        def dinicDFS(u, f):
            if u == sink:
                return f
            for v, w in enumerate(self.graph[u]):
                if level[u] + 1 == level[v] and w:
                    t = dinicDFS(v, min(f, w))
                    if t > 0:
                        self.graph[u][v] -= t
                        self.graph[v][u] += t
                        return t

            return 0

        while dinicBFS():
            while True:
                d = dinicDFS(source, float('inf'))
                maxFlow += d
                if not d:
                    break

        return maxFlow

    def _searchPathByDFS(self, s, t, parent):
        visited = [False] * self.ROW
        visited[s] = True

        def _dfs(u):
            if u == t:
                return
            for v, w in enumerate(self.graph[u]):
                if w > 0 and not visited[v]:
                    parent[v] = u
                    visited[v] = True
                    _dfs(v)

        _dfs(s)
        return True if visited[t] else False

    def fordFulkerson(self, source, sink):
        """
        :param source: 源点
        :param sink: 终点
        :return:
        """
        maxFlow = 0
        parent = [-1] * self.ROW
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]
        while self._searchPathByDFS(source, sink, parent):
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
                self.graph[v][u] += pathFlow
                v = parent[v]
        return maxFlow

    def fordFulkerson2(self, source, sink):
        """
        :param source: 源点
        :param sink: 终点
        :return:
        """
        maxFlow = 0
        source = self.vertex2idx[source]
        sink = self.vertex2idx[sink]

        def _dfs(u, cur):
            if u == sink:
                return cur
            visited[u] = True
            for v, w in enumerate(self.graph[u]):
                if not visited[v] and w > 0:
                    d = _dfs(v, min(cur, w))
                    if d > 0:
                        self.graph[u][v] -= d
                        self.graph[v][u] += d
                        return d
            return 0

        while True:
            visited = [False] * self.ROW
            f = _dfs(source, float('inf'))
            if f == 0:
                return maxFlow
            maxFlow += f
        # return maxFlow

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

    def pushRelabel2(self, source, sink):
        """
        计算最大流有2种方法：
        1、fordFulkerson是一种方法，有不同实现方式寻找增广路径，本程序使用bfs
        2、推送-重贴标签（也叫预流推进算法）
        方法2的改进算法
        返回最大流
        :param source: 源点
        :param sink: 终点
        :return:
        """

        return 0


if __name__ == "__main__":
    # 1.单向图，矩阵表示
    vertex = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    edge = [['s', 'v1', 16], ['s', 'v2', 13], ['v1', 'v3', 12], ['v2', 'v1', 4], ['v2', 'v4', 14], ['v3', 'v2', 9],
            ['v3', 't', 20], ['v4', 'v3', 7], ['v4', 't', 4]]
    g = DirectionGraph(vertex, edge)
    source = 's'
    sink = 't'
    maxFlow = g.dinic(source, sink)
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
    maxFlow = g.edmondsKarp(source, sink)
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
