#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/20 17:11:24
@Author  : pengyuan.li
@File    : 0x02-divide.py
@Software: VSCode
'''

# here put the import lib
from copy import deepcopy


# 费解的开关
def minSteps(mat):
    """
    mat:0/1组成的n*n矩阵，更改元素i，则周边元素取反
    return:最少的步数使得矩阵元素全部为1，与书上相反（需修改代码，k>>i ^ 1,mat[i][j]==0,即对元素0进行操作）。
    """
    dx, dy = [0, 0, 0, -1, 1], [0, -1, 1, 0, 0]
    N = len(mat)

    def change(x, y):
        for i in range(N):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                mat[nx][ny] ^= 1

    res = float('inf')
    for k in range(1 << N):
        cnt = 0
        backupMat = deepcopy(mat)
        # 第1行
        for i in range(N):
            if k >> i & 1:
                change(0, i)
                cnt += 1
        # print(mat,cnt)
        # 第i+1行
        for i in range(N - 1):
            for j in range(N):
                if mat[i][j] == 0:
                    change(i + 1, j)
                    cnt += 1
        # print(mat,cnt)
        isSuccess = True
        for i in range(N):
            if mat[N - 1][i] == 0:
                isSuccess = False
                break
        if isSuccess:
            res = min(res, cnt)
        mat = deepcopy(backupMat)
    return res


def hanoi4(n):
    """
    经典hanoi塔的变形，4塔，求最少移动次数
    3塔，d[i] = 2*d[i-1]+1
    4塔，f[n] = min(2*f[i]+d[n-i])
    """
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = 2 * d[i - 1] + 1
    f = [float('inf')] * (n + 1)
    f[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            f[i] = min(f[i], 2 * f[j] + d[i - j])
    return f[n]


import math


def fractal(queries):
    """
    queries:[城市等级，房屋A，房屋B]
    return:dist(A,B)
    城市规划，分形
    """

    def calc(n, m):
        if n == 0:
            return 0, 0
        lens = 1 << (n - 1)
        cnt = 1 << (2 * n - 2)
        px, py = calc(n - 1, m % cnt)
        z = m // cnt
        if z == 0:
            return py, px
        elif z == 1:
            return px, py + lens
        elif z == 2:
            return px + lens, py + lens

        return 2 * lens - 1 - py, lens - 1 - px

    for n, a, b in queries:
        ax, ay = calc(n, a - 1)
        bx, by = calc(n, b - 1)
        print(math.sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by)))
    pass


if __name__ == "__main__":
    mat = [[0, 0, 1, 1, 1], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 0],
           [1, 1, 1, 0, 0]]
    print(minSteps(mat))
    print(hanoi4(5))
    queries = [[1, 1, 2], [2, 16, 1], [3, 4, 33]]
    print(fractal(queries))