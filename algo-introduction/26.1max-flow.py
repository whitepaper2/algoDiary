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

    def printPathByBFS(self, s, t, originGraph):

        flowGraph = list()
        for g1, g2 in zip(originGraph, self.graph):
            cur = list()
            for c1, c2 in zip(g1, g2):
                if c2 >= 0:
                    cur.append(c1 - c2)
                else:
                    cur.append(0)
            flowGraph.append(cur)
        visited = [False] * self.ROW
        queue = deque()
        queue.append(s)
        path = dict()
        visited[s] = True
        while queue:
            cur = queue.popleft()
            for idx, cap in enumerate(flowGraph[cur]):
                if cap > 0:
                    path[(cur, idx)] = cap
                    # if not visited[idx]:
                    queue.append(idx)
                    # visited[idx] = True
        return path


if __name__ == "__main__":
    # 1.单向图
    # graph = [[0, 8, 0, 0, 3, 0],
    #          [0, 0, 9, 0, 0, 0],
    #          [0, 0, 0, 0, 7, 2],
    #          [0, 0, 0, 0, 0, 5],
    #          [0, 0, 0, 4, 0, 0],
    #          [0, 0, 0, 0, 0, 0]]
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 0, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]
    # todo:形成环或双向边
    graph2 = deepcopy(graph)
    g = DirectionGraph(graph)
    source = 0
    sink = 5
    maxFlow = g.fordFulkerson(0, 5)
    print("maxFlow={}".format(maxFlow))
    print(g.printPathByBFS(source, sink, graph2))
