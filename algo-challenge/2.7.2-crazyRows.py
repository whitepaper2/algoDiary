#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/13 上午10:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.7.2-crazyRows.py
# @Software: PyCharm

from typing import List


def crazyRows(mat: List[List[int]]) -> int:
    """
    交换相邻行，得到下三角矩阵，求最少的交换次数
    :param mat:
    :return:
    """
    N = len(mat)
    res = 0
    position = [-1] * N
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                position[i] = j - 1
                break
    for i in range(N):
        pos = -1
        for j in range(i, N):
            if position[j] <= i:
                pos = j
                break
        for k in range(pos, i, -1):
            position[k], position[k - 1] = position[k - 1], position[k]
            res += 1
    return res


def prisoners(P: int, Q: int, A: List[int]) -> int:
    """
    识别A中囚犯需要付出的金币数
    :param P: 总的监狱房间个数
    :param Q:
    :param A:
    :return:
    """
    A.insert(0, 0)
    A.append(P + 1)
    dp = [[float('inf') for _ in range(Q + 2)] for _ in range(Q + 1)]
    for i in range(Q + 1):
        dp[i][i + 1] = 0

    for w in range(2, Q + 2):
        i = 0
        while i + w <= Q + 1:
            j = i + w
            t = float('inf')
            for k in range(i + 1, j):
                t = min(t, dp[i][k] + dp[k][j])
            dp[i][j] = t + A[j] - A[i] - 2
            i += 1

    return dp[0][Q + 1]


def lightonoff(N: int, light: List[str]) -> (int, int):
    """
    步长、最少反转次数
    :param N:
    :param light:
    :return:
    """
    light2arr = []
    for e in light:
        light2arr.append(1 if e == 'B' else 0)

    def calc(K):
        f = [0] * (N + 1)
        res = 0
        curSum = 0
        i = 0
        while i + K <= N:
            if (light2arr[i] + curSum) % 2 != 0:
                res += 1
                f[i] = 1
            curSum += f[i]
            if i - K + 1 >= 0:
                curSum -= f[i - K + 1]
            i += 1

        for i in range(N - K + 1, N):
            if (light2arr[i] + curSum) % 2 != 0:
                return -1
            if i - K + 1 >= 0:
                curSum -= f[i - K + 1]
        return res

    K = 1
    M = N
    for k in range(1, N + 1):
        m = calc(k)
        if 0 <= m < M:
            K = k
            M = m
    return K, M


if __name__ == "__main__":
    matrix = [[1, 1, 1, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
    print(crazyRows(matrix))

    p = 20
    q = 3
    A = [3, 6, 14]
    print(prisoners(p, q, A))

    n = 7
    light = ['B', 'B', 'F', 'B', 'F', 'B', 'B']
    print(lightonoff(n, light))
