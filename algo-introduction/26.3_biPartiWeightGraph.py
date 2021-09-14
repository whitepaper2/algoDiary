#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 下午7:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.2_binaryPartitionGraph.py
# @Software: PyCharm

"""
二分图的带权重最大匹配，使得匹配边的权重之和最大
1、费用流算法
2、KM算法，匈牙利算法的变形，适用在完备二分图上
"""


class UndirectionGraph(object):
    def __init__(self, graph):
        """
        :param graph:图的邻接矩阵
        """
        N = 100
        self.graph = graph
        self.ROW = len(graph)
        self.match = [-1000] * N
        # 左、右顶标，以及是否访问过
        self.la = [-1] * N
        self.lb = [-1] * N
        self.va = [False] * N
        self.vb = [False] * N
        self.upd = [1e10] * N
        self.delta = 1e9

    def _dfs(self, x):
        """
        深度优先遍历，寻找交错路径
        :param x: 节点
        :return: True/False
        """
        self.va[x] = True
        for y in range(self.ROW):
            if not self.vb[y]:
                if self.la[x] + self.lb[y] - self.graph[x][y] == 0:
                    self.vb[y] = True
                    if self.match[y] == -1000 or self._dfs(self.match[y]):
                        self.match[y] = x
                        return True
                else:
                    self.upd[y] = min(self.upd[y], self.la[x] + self.lb[y] - self.graph[x][y])

        return False

    def getMaxMatchCost(self):
        res = 0
        for i in range(self.ROW):
            self.la[i] = float("-inf")
            self.lb[i] = 0
            for j in range(self.ROW):
                self.la[i] = max(self.la[i], self.graph[i][j])

        for i in range(self.ROW):
            while True:
                self.va = [False] * len(self.va)
                self.vb = [False] * len(self.vb)
                for j in range(self.ROW):
                    self.upd[j] = 1e10
                if self._dfs(i):
                    break
                for j in range(self.ROW):
                    if not self.vb[j]:
                        self.delta = min(self.delta, self.upd[j])
                for j in range(self.ROW):
                    if self.va[j]:
                        self.la[j] -= self.delta
                    if self.vb[j]:
                        self.lb[j] += self.delta
        for i in range(self.ROW):
            res += self.graph[self.match[i]][i]
        return res

    def printMatch(self):
        for i, v in enumerate(self.match):
            if v != -1000:
                print(v, i)


if __name__ == "__main__":
    # students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    # mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    students = [[1, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 1, 0]]
    mentors = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0]]
    n = len(students)
    score = [[0] * n for _ in range(n)]
    for i, stu in enumerate(students):
        for j, men in enumerate(mentors):
            score[i][j] = sum([1 for u, v in zip(stu, men) if u == v])
    g = UndirectionGraph(score)
    print(g.graph)
    print(g.getMaxMatchCost())
    g.printMatch()
