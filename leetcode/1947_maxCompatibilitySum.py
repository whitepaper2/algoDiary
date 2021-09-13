#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 下午2:31
# @Author  : pengyuan.li
# @Site    : 
# @File    : 1947_maxCompatibilitySum.py
# @Software: PyCharm

"""
leetcode-251 weekly contest
学生和老师答案，数值相同的加1，找出最优匹配方案，使得和最大
students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
"""

from collections import deque
from copy import deepcopy


class DirectionGraph(object):
    def __init__(self, graph):
        self.ROW = len(graph)
        self.graph = graph
        self.rawGraph = deepcopy(graph)

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

    def printPathByBFS(self, s):
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
                    path[(cur, idx)] = cap
                    queue.append(idx)
        return path


def bruteSearch(students, mentors):
    """
    暴力搜索
    :param students: 学生打分
    :param mentors: 老师打分
    :return:
    """
    n = len(students)
    score = [[0] * n for _ in range(n)]
    for i, stu in enumerate(students):
        for j, men in enumerate(mentors):
            score[i][j] = sum([1 for u, v in zip(stu, men) if u == v])
    res = float('-inf')

    def traceBack(step, cur):
        nonlocal res
        if step == n:
            curSum = 0
            for x, y in zip(range(n), cur):
                curSum += score[x][y]
            if curSum > res:
                res = curSum
            return
        for i in range(n):
            if i not in cur:
                cur.append(i)
                traceBack(step + 1, cur)
                cur.pop()

    traceBack(0, [])
    return res


if __name__ == "__main__":
    # students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    # mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    students = [[1, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 1, 0]]
    mentors = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0]]
    print(bruteSearch(students, mentors))

    # todo:最大流算法，不能解决完全匹配问题
    students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    # 增加源点和终点，转为求单源点、单终点的最大流问题
    n = len(students) + len(mentors) + 2
    score = [[0] * n for _ in range(n)]
    for i, stu in enumerate(students):
        for j, men in enumerate(mentors):
            score[i][len(students) + j] = sum([1 for u, v in zip(stu, men) if u == v])
    s = n - 2
    t = n - 1
    for i in range(len(students)):
        score[s][i] = 1
    for i in range(len(students), s):
        score[i][t] = 1
    g = DirectionGraph(score)
    maxFlow = g.fordFulkerson(s, t)
    print("maxFlow={}".format(maxFlow))
    print(g.printPathByBFS(s))
    # todo:km,解决带权重的二分图完全匹配问题
    # 最大流求解二分图匹配个数，增加1源点、1终点
    vertex = ["l1", "l2", "l3", "l4", "r1", "r2", "r3", "r4", "s", "t"]
    edge = [["l1", "r1"], ["l1", "r2"], ["l2", "r2"], ["l2", "r3"], ["l3", "r1"], ["l3", "r2"], ["l4", "r3"],
            ["s", "l1"],
            ["s", "l2"], ["s", "l3"], ["s", "l4"], ["r1", "t"], ["r2", "t"], ["r3", "t"], ["r4", "t"]]
    vertex2Idx = dict()
    graph = [[0] * len(vertex) for _ in range(len(vertex))]
    for i, v in enumerate(vertex):
        vertex2Idx[v] = i
    for u, v in edge:
        graph[vertex2Idx[u]][vertex2Idx[v]] = 1
    g = DirectionGraph(graph)
    print(g.fordFulkerson(vertex2Idx["s"], vertex2Idx["t"]))
