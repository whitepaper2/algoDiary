#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/05 11:20:42
@Author  : pengyuan.li
@File    : 3.5.7-evacuation.py
@Software: VSCode
'''

# here put the import lib
from typing import List
from collections import defaultdict, deque


class Solution(object):

    def escapeTime(self, maze: List[List[str]]) -> str:
        rows, cols = len(maze), len(maze[0])
        doors = []
        peoples = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dist = [[[[-1 for _ in range(cols)] for _ in range(rows)]
                 for _ in range(cols)] for _ in range(rows)]

        def _getDistBybfs(i, j, d):
            d[i][j] = 0
            queue = deque()
            queue.append((i, j))
            while queue:
                curx, cury = queue.popleft()
                for dx, dy in directions:
                    x, y = curx + dx, cury + dy
                    if 0 <= x < rows and 0 <= y < cols and maze[x][
                            y] == '.' and d[x][y] < 0:
                        d[x][y] = d[curx][cury] + 1
                        queue.append((x, y))

        # 二分圖求最大匹配個數
        class BiGraph():

            def __init__(self, nums) -> None:
                self.graph = defaultdict(list)
                self.used = [0] * nums
                self.match = [-1] * nums
                self.maxN = nums

            def addEdge(self, u, v):
                self.graph[u].append(v)
                self.graph[v].append(u)

            def dfs(self, v):
                self.used[v] = 1
                for u in self.graph[v]:
                    w = self.match[u]
                    if w < 0 or self.used[w] == 0 and self.dfs(w):
                        self.match[v] = u
                        self.match[u] = v
                        return True
                return False

            def matchNums(self):
                res = 0
                for i in range(self.maxN):
                    if self.match[i] < 0:
                        self.used = [0] * self.maxN
                        if self.dfs(i):
                            res += 1
                return res

        def _isValid(t):
            d, p = len(doors), len(peoples)
            v = t * d + p
            G = BiGraph(v)
            for i in range(d):
                for j in range(p):
                    if dist[doors[i][0]][doors[i][1]][peoples[j][0]][peoples[j]
                                                                     [1]] >= 0:
                        for k in range(
                                dist[doors[i][0]][doors[i][1]][peoples[j][0]][
                                    peoples[j][1]], t + 1):
                            G.addEdge((k - 1) * d + i, t * d + j)

            return G.matchNums() == p

        # 每个门入口下人对应的最短路径
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == 'D':
                    doors.append((i, j))
                    _getDistBybfs(i, j, dist[i][j])
                elif maze[i][j] == '.':
                    peoples.append((i, j))

        # 1、二分法求最小时间
        n = rows * cols
        # left, right = -1, n + 1
        # while right - left > 1:
        #     mid = (right + left) // 2
        #     if _isValid(mid):
        #         right = mid
        #     else:
        #         left = mid

        # return "impossible" if right > n else right
        # 2、增广路径，不用重复计算
        num = 0
        d, p = len(doors), len(peoples)
        v = n * d + p
        G = BiGraph(v)
        for i in range(d):
            for j in range(p):
                if dist[doors[i][0]][doors[i][1]][peoples[j][0]][peoples[j]
                                                                 [1]] >= 0:
                    for k in range(
                            dist[doors[i][0]][doors[i][1]][peoples[j][0]][
                                peoples[j][1]], n + 1):
                        G.addEdge((k - 1) * d + i, n * d + j)
        if p == 0:
            return 0
        for v in range(n * d):
            G.used = [0] * G.maxN
            if G.dfs(v):
                num += 1
                if num == p:
                    return v // d + 1
        return "impossible"


if __name__ == "__main__":
    maze = [['X', 'X', 'D', 'X', 'X'], ['X', '.', '.', '.', 'X'],
            ['D', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'D'],
            ['X', 'X', 'X', 'X', 'X']]
    ss = Solution()
    print(ss.escapeTime(maze))

    maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'D'],
            ['X', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
    ss = Solution()
    print(ss.escapeTime(maze))

    maze = [['X', 'D', 'X', 'X', 'X'], ['X', '.', 'X', '.', 'D'],
            ['X', 'X', '.', 'X', 'X'], ['D', '.', 'X', '.', 'X'],
            ['X', 'X', 'X', 'D', 'X']]
    ss = Solution()
    print(ss.escapeTime(maze))
