#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 下午4:35
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.1max-flow.py
# @Software: PyCharm

# 最大流最小切割算法

from collections import deque


class DirectionGraph(object):
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searchPathByBFS(self, s, t, parent):
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
        返回最大流
        :param source: 源点
        :param sink: 终点
        :return:
        """
        maxFlow = 0
        parent = [-1] * self.ROW
        while self.searchPathByBFS(source, sink, parent):
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


if __name__ == "__main__":
    graph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    g = DirectionGraph(graph)
    source = 0
    sink = 5
    maxFlow = g.fordFulkerson(0, 5)
    print(maxFlow)
