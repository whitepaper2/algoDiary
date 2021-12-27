#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 下午4:48
# @Author  : pengyuan.li
# @Site    : 
# @File    : 26.2-biPartiGraph.py
# @Software: PyCharm


"""
匹配问题：
    1.二分图匹配
        1.1最大流算法，添加虚拟节点：源点和汇点，权重1
        1.2匈牙利算法(Hagarian)->fordFulkerson 类似
        1.3hopcroft-karp算法->dinic 类似
        @todo:上述算法怎么类似的？增广路算法<=>最大流，输入矩阵不同
    2.一般匹配
        NP-hard，结对子问题：2N个学生两两结合，每个学生只想和自己的朋友结对子，求最多能结成多少对？
"""
# 二分图求最大匹配个数，匈牙利算法
from collections import defaultdict, deque


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
        # 右边匹配左边
        self.leftLen = len(leftVertex)
        self.rightLen = len(rightVertex)
        self.leftMatch = [-1] * self.leftLen
        self.rightMatch = [-1] * self.rightLen
        self.used = [False] * self.rightLen

        self.graph = [[0] * self.rightLen for _ in range(self.leftLen)]
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

    def hopcroftkarp(self):
        leftDist = [-1] * self.leftLen
        rightDist = [-1] * self.rightLen
        dis = float('inf')

        def _bfs():
            nonlocal leftDist, rightDist, dis
            dis = float('inf')
            leftDist = [-1] * self.leftLen
            rightDist = [-1] * self.rightLen
            queue = deque()
            for i in range(self.leftLen):
                if self.leftMatch[i] == -1:
                    queue.append(i)
                    leftDist[i] = 0
            while queue:
                u = queue.popleft()
                if leftDist[u] > dis:
                    break
                for v, w in enumerate(self.graph[u]):
                    if w > 0 and rightDist[v] == -1:
                        rightDist[v] = leftDist[u] + 1
                        if self.rightMatch[v] == -1:
                            dis = rightDist[v]
                        else:
                            leftDist[self.rightMatch[v]] = rightDist[v] + 1
                            queue.append(self.rightMatch[v])

            return dis != float('inf')

        def _dfs(u):
            nonlocal leftDist, rightDist, dis
            for v, w in enumerate(self.graph[u]):
                if w > 0 and not self.used[v] and leftDist[u] + 1 == rightDist[v]:
                    self.used[v] = True
                    if self.rightMatch[v] != -1 and rightDist[v] == dis:
                        continue
                    if self.rightMatch[v] == -1 or _dfs(self.rightMatch[v]):
                        self.leftMatch[u] = v
                        self.rightMatch[v] = u
                        return True
            return False

        res = 0
        while _bfs():
            self.used = [False] * self.rightLen
            for i in range(self.leftLen):
                if self.leftMatch[i] == -1 and _dfs(i):
                    res += 1
        return res

    def printMatch(self):
        for i, v in enumerate(self.rightMatch):
            if v != -1:
                print(self.leftIdx2Vertex[v], self.rightIdx2Vertex[i])


if __name__ == "__main__":
    leftVertex = ["l1", "l2", "l3", "l4"]
    rightVertex = ["r1", "r2", "r3", "r4"]
    # edge = [["l1", "r1"], ["l1", "r2"], ["l2", "r2"], ["l2", "r3"], ["l3", "r1"], ["l3", "r2"], ["l4", "r3"]]
    edge = [["l1", "r1"], ["l2", "r1"], ["l2", "r3"], ["l2", "r4"], ["l3", "r2"], ["l3", "r4"], ["l4", "r3"]]
    g = UndirectionGraph(leftVertex, rightVertex, edge)
    print(g.graph)
    print(g.hopcroftkarp())
    g.printMatch()
