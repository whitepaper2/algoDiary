#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/04 10:52:11
@Author  : pengyuan.li
@File    : week274.py
@Software: VSCode
'''

# here put the import lib
"""
2127. 参加会议的最多员工数
一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。
员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。
给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 
"""

from collections import defaultdict
from typing import List


class Solution:

    def maximumInvitations(self, favorite: List[int]):
        """
        有两种情况：1、部分员工组成一个环，计算最长环的长度；
        2、员工分为若干组，即二元环，在两个端点计算最长链
        """
        adj = defaultdict(set)
        n = len(favorite)
        color = [0] * n
        dist = [0] * n
        self.maxcnt = 0
        pairs2 = []
        for i, v in enumerate(favorite):
            adj[v].add(i)

        def _dfs(u):
            color[u] = 1
            for v in adj[u]:
                if color[v] == 0:
                    dist[v] = dist[u] + 1
                    _dfs(v)
                elif color[v] == 1:
                    tmpcnt = dist[u] - dist[v] + 1
                    self.maxcnt = max(self.maxcnt, tmpcnt)
                    if tmpcnt == 2:
                        pairs2.append((u, v))
            color[u] = 2

        def _dfs2(u, p, d):
            maxDepth = d
            for v in adj[u]:
                if v != p:
                    maxDepth = max(maxDepth, _dfs2(v, p, d + 1))
            return maxDepth

        for i in range(n):
            if color[i] == 0:
                _dfs(i)
        fromPairs = 0
        for u, v in pairs2:
            fromPairs += _dfs2(u, v, 1)
            fromPairs += _dfs2(v, u, 1)

        print(max(self.maxcnt, fromPairs))


if __name__ == "__main__":
    # favorite = [2,2,1,2]
    favorite = [1, 0]
    s = Solution()
    s.maximumInvitations(favorite)
