#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def matrixMultiply(p):
    """
    矩阵最优乘法，s[i,j]=min(s[i,k]+s[k+1,j]+p[i-1]*p[k]*p[j] , k=i,2,...j-1
    :param p:
    :return:s[1,len(p)-1]
    """
    n = len(p) - 1
    r = [0] * (n + 1)
    s = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    c = 1  # 每次截断的成本
    for i in range(n, -1, -1):
        for j in range(i, n + 1):
            if i == j:
                s[i][j] = 0
            else:
                for k in range(i, j):
                    if s[i][j] > s[i][k] + s[k + 1][j] + p[i - 1] * p[k] * p[j]:
                        s[i][j] = s[i][k] + s[k + 1][j] + p[i - 1] * p[k] * p[j]

    return s[1][n]


def memoCutRod(p, n):
    r = [float("-inf")] * (n + 1)
    s = [0] * (n + 1)

    def subMemoCurRod(p, i, r, s):
        if r[i] >= 0:
            return r[i]
        if i == 0:
            q = 0
        else:
            q = float('-inf')
            for j in range(1, i + 1):
                # q = max(q, p[j] + subMemoCurRod(p, i - j, r))
                if q < p[j] + subMemoCurRod(p, i - j, r, s):
                    q = p[j] + subMemoCurRod(p, i - j, r, s)
                    s[i] = j
        r[i] = q
        return q

    return subMemoCurRod(p, n, r, s), s


if __name__ == "__main__":
    p = [5, 10, 3, 12, 5, 50, 6]
    print(matrixMultiply(p))
