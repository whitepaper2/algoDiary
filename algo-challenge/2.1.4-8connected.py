#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 下午4:48
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1.4-8connected.py
# @Software: PyCharm


def lakeCount(graden):
    """
    求积水块数
    :param graden:
    :return:
    """
    n, m = len(graden), len(graden[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    def dfs(row, col, visited):
        visited[row][col] = 1
        for dx, dy in direction:
            x, y = row + dx, col + dy
            if 0 <= x < n and 0 <= y < m and graden[x][y] == 'W' and visited[x][y] == 0:
                dfs(x, y, visited)

    res = 0
    for r in range(n):
        for c in range(m):
            if visited[r][c] == 0 and graden[r][c] == 'W':
                dfs(r, c, visited)
                res += 1

    return res


def lakeCount2(graden):
    """
    求积水块数，消灭'W'，修改原院子分布
    :param graden:
    :return:
    """
    n, m = len(graden), len(graden[0])
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    def dfs(row, col):
        graden[row][col] = '.'
        for dx, dy in direction:
            x, y = row + dx, col + dy
            if 0 <= x < n and 0 <= y < m and graden[x][y] == 'W':
                dfs(x, y)

    res = 0
    for r in range(n):
        for c in range(m):
            if graden[r][c] == 'W':
                dfs(r, c)
                res += 1

    return res


if __name__ == "__main__":
    graden = [['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
              ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
              ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
              ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
              ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
              ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
              ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
              ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']]
    print(lakeCount(graden))
    print(lakeCount2(graden))
    print(graden)
