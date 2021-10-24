#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 下午6:48
# @Author  : pengyuan.li
# @Site    : 
# @File    : week264.py
# @Software: PyCharm
"""
5908. 统计最高分的节点数目

给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，
其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，
剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        """
        构成无向图，dfs遍历每个子树的个数
        :param parents:
        :return:
        """
        n = len(parents)
        neighbors = defaultdict(list)
        for i, p in enumerate(parents):
            neighbors[p].append(i)
            if p != -1:
                neighbors[i].append(p)
        neighbors.pop(-1)
        self.cnt = 0

        def dfs(p, isVisited, neighbors):
            for p2 in neighbors[p]:
                if not isVisited[p2]:
                    isVisited[p2] = True
                    self.cnt += 1
                    dfs(p2, isVisited, neighbors)

        def calcCnts(isVisited, points, neighbors):
            cnts = list()
            for p in points:
                if p != -1 and not isVisited[p]:
                    self.cnt = 1
                    isVisited[p] = True
                    dfs(p, isVisited, neighbors)
                    cnts.append(self.cnt)
            res = 1
            for c in cnts:
                res = res * c
            return res

        cntList = []
        for k, v in neighbors.items():
            isVisited = {x: False for x in range(n)}
            isVisited[k] = True

            cntList.append(calcCnts(isVisited, v, neighbors))
        cntList.sort()
        return cntList.count(cntList[-1])

    def countHighestScoreNodes2(self, parents: List[int]) -> int:
        n = len(parents)
        neighbors = defaultdict(list)
        for i in range(1, n):
            neighbors[parents[i]].append(i)
        cntDict = [0] * n
        self.hi = 0
        self.hiCnt = 0

        def dfs(u, cntDict):
            cntDict[u] = 1
            for v in neighbors[u]:
                dfs(v, cntDict)
                cntDict[u] += cntDict[v]
            rem = max(1, n - cntDict[u])
            for v in neighbors[u]:
                rem *= cntDict[v]
            if rem > self.hi:
                self.hi = rem
                self.hiCnt = 0

            if rem == self.hi:
                self.hiCnt += 1

        dfs(0, cntDict)
        return self.hiCnt


"""
5909. 并行课程 III
给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，
表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，
其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。

请你根据以下规则算出完成所有课程所需要的 最少 月份数：

如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
你可以 同时 上 任意门课程 。
请你返回完成所有课程所需要的 最少 月份数。

注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。

"""


def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    """
    拓扑顺序遍历，更新最大值
    :param n:
    :param relations:
    :param time:
    :return:
    """
    adj = defaultdict(list)
    degree = [0] * n
    for u, v in relations:
        u2 = u - 1
        v2 = v - 1
        adj[u2].append(v2)
        degree[v2] += 1
    queue = deque()
    dp = [0] * n
    for i in range(n):
        if degree[i] == 0:
            queue.append(i)
    while queue:
        u = queue.popleft()
        dp[u] += time[u]
        for v in adj[u]:
            dp[v] = max(dp[v], dp[u])
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)
    return max(dp)


if __name__ == "__main__":
    parents = [-1, 2, 0, 2, 0]
    ss = Solution()
    print(ss.countHighestScoreNodes(parents))
    print(ss.countHighestScoreNodes2(parents))

    n = 3
    relations = [[1, 3], [2, 3]]
    time = [3, 2, 5]
    print(minimumTime(n, relations, time))
