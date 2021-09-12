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

    def bipartiteMatch(self):
        # d = float('inf')
        maxVal = 100000
        d = maxVal
        curSum = 0
        maxSize = 20
        ly = [0] * maxSize
        lx = [0] * maxSize
        n = self.ROW
        # for i in range(1, n):
        #     lx[i] = float('-inf')
        #     for j in range(1, n):
        #         lx[i] = max(lx[i], self.graph[i][j])
        print(lx)
        link = [-1] * maxSize
        visx = [False] * maxSize
        visy = [False] * maxSize

        def can(t):
            visx[t] = True
            for k in range(1, n):
                if not visy[k] and lx[t] + ly[k] == self.graph[t][k]:
                    visy[k] = True
                    if link[k] == -1 or can(link[k]):
                        link[k] = t
                        return True
            return False

        live = 0
        perfect = False
        for i in range(1, n):
            for i2 in range(1, n):
                lx[i2] = float('-inf')
                for j2 in range(1, n):
                    lx[i2] = max(lx[i2], self.graph[i2][j2])
            print(i)
            iters = 0
            while True:
                if can(i):
                    break
                for j in range(1, n):
                    if visy[j]:
                        for k in range(1, n):
                            if not visy[k]:
                                d = min(d, lx[j] + ly[k] - self.graph[j][k])

                if d == maxVal:
                    return -1
                if d == 0:
                    break
                for j in range(1, n):
                    if visx[j]:
                        lx[j] -= d
                for j in range(1, n):
                    if visy[j]:
                        ly[j] += d
                print(d, lx, ly)
                iters += 1

        for i in range(1, n):
            if link[i] > -1:
                curSum += self.graph[link[i]][i]
                print("match {}-{}".format(link[i], i))
        return curSum


if __name__ == "__main__":
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
    # todo:匈牙利算法,km,解决带权重的二分图完全匹配问题
    # students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    # mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    # students = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 0]]
    # mentors = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1]]

    # students = [[0, 1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 1],
    #             [1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0]]
    # mentors = [[1, 0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0],
    #            [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1]]
    students = [[1, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 1, 0]]
    mentors = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0]]
    n = len(students)
    score = [[0] * (n + 1) for _ in range(n + 1)]
    for i, stu in enumerate(students):
        for j, men in enumerate(mentors):
            score[i + 1][j + 1] += sum([1 for u, v in zip(stu, men) if u == v])
    print(score)
    g = DirectionGraph(score)
    maxScore = g.bipartiteMatch()
    print("maxScore={}".format(maxScore))
