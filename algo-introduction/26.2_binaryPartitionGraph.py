#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 下午7:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.2_binaryPartitionGraph.py
# @Software: PyCharm


# 二分图求最大匹配个数，匈牙利算法
from collections import defaultdict


class UndirectionGraph(object):
    def __init__(self, leftVertex, rightVertex, edge):
        self.vertex = leftVertex + rightVertex
        self.edge = edge
        self.leftVertex2Idx = dict()
        self.rightVertex2Idx = dict()
        self.leftIdx2Vertex = dict()
        self.rightIdx2Vertex = dict()
        for i, v in enumerate(leftVertex):
            self.leftVertex2Idx[v] = i
            self.leftIdx2Vertex[i] = v
        for i, v in enumerate(rightVertex):
            self.rightVertex2Idx[v] = i
            self.rightIdx2Vertex[i] = v
        self.match = [-1] * len(rightVertex)
        self.used = [False] * len(rightVertex)
        self.leftLen = len(leftVertex)
        self.rightLen = len(rightVertex)
        self.graph = [[0] * len(rightVertex) for _ in range(len(leftVertex))]
        for u, v in edge:
            self.graph[self.leftVertex2Idx[u]][self.rightVertex2Idx[v]] = 1

    def checkBiPartiGraph(self):
        """
        检测该图是否为二分图，当且仅当不存在奇数环
        相邻节点着不同颜色
        :return:
        """
        neighbor = defaultdict(list)
        for u, v in self.edge:
            neighbor[u].append(v)
            neighbor[v].append(u)
        color = {u: 0 for u in self.vertex}

        def dfs(i, c):
            color[i] = c

            for j in neighbor[i]:
                if color[j] == 0:
                    dfs(j, 3 - c)
                elif color[j] == color:
                    return False

        for u in self.vertex:
            if color[u] == 0:
                dfs(u, 1)
        return True

    def _dfs(self, x):
        """
        深度优先遍历，寻找交错路径
        :param x: 节点
        :return: True/False
        """
        for j in range(self.rightLen):
            if self.graph[x][j] and not self.used[j]:
                self.used[j] = True
                if self.match[j] == -1 or self._dfs(self.match[j]):
                    self.match[j] = x
                    return True
        return False

    def getMatchCnts(self):
        res = 0
        for i in range(self.leftLen):
            self.used = [False] * self.rightLen
            if self._dfs(i):
                res += 1
        return res

    def printMatch(self):
        for i, v in enumerate(self.match):
            if v != -1:
                print(self.leftIdx2Vertex[v], self.rightIdx2Vertex[i])


if __name__ == "__main__":
    leftVertex = ["l1", "l2", "l3", "l4"]
    rightVertex = ["r1", "r2", "r3", "r4"]
    edge = [["l1", "r1"], ["l1", "r2"], ["l2", "r2"], ["l2", "r3"], ["l3", "r1"], ["l3", "r2"], ["l4", "r3"]]
    g = UndirectionGraph(leftVertex, rightVertex, edge)
    print(g.graph)
    print(g.getMatchCnts())
    g.printMatch()
    print(g.checkBiPartiGraph())
