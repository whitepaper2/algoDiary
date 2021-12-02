#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 下午8:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1.4-mazeMindistance.py
# @Software: PyCharm


from collections import deque


def minDistance(maze):
    """
    求迷宫从起点到终点的最小步数
    :param maze:
    :return:
    """
    n, m = len(maze), len(maze[0])
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                startPx, startPy = i, j
            if maze[i][j] == 'G':
                endPx, endPy = i, j
    dist[startPx][startPy] = 0
    queue = deque()
    queue.append((startPx, startPy))
    while queue:
        x, y = queue.pop()
        if x == endPx and y == endPy:
            break
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            tx, ty = x + dx, y + dy
            if 0 <= tx < n and 0 <= ty < m and maze[tx][ty] != '#' and dist[tx][ty] == float('inf'):
                dist[tx][ty] = dist[x][y] + 1
                queue.append((tx, ty))
    return dist[endPx][endPy]


if __name__ == "__main__":
    maze = [['#', 'S', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
            ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
            ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
            ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
            ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#']]
    print(minDistance(maze))
