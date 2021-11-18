#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 下午4:37
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x51-takePhoto.py
# @Software: PyCharm


def picturePermutations(k, people):
    """
    从左到右按身高降序排序、从前到后降序排序，求一共能组成多少中排列方式
    :param k:总排数,1<=k<=5
    :param people:长度为k的数组,sum(people)<=30
    :return:
    """
    maxN = 31
    s = people + [0] * (5 - k)
    f = [[[[[0 for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)] for _ in
         range(maxN)]
    f[0][0][0][0][0] = 1
    # f = [[[0 for _ in range(maxN)] for _ in range(maxN)] for _ in range(maxN)]

    for a in range(s[0] + 1):
        for b in range(min(a, s[1]) + 1):
            for c in range(min(b, s[2]) + 1):
                for d in range(min(c, s[3]) + 1):
                    for e in range(min(d, s[4]) + 1):
                        if a and a - 1 >= b:
                            f[a][b][c][d][e] += f[a - 1][b][c][d][e]
                        if b and b - 1 >= c:
                            f[a][b][c][d][e] += f[a][b - 1][c][d][e]
                        if c and c - 1 >= d:
                            f[a][b][c][d][e] += f[a][b][c - 1][d][e]
                        if d and d - 1 >= e:
                            f[a][b][c][d][e] += f[a][b][c][d - 1][e]
                        if e:
                            f[a][b][c][d][e] += f[a][b][c][d][e - 1]
    return f[s[0]][s[1]][s[2]][s[3]][s[4]]


def lcis(A, B):
    """
    最长上升公共子序列，即最长上升子序列+最长公共子序列
    F[i,j] = F[i-1,j], A[i]!=B[j]
           = max(F[i-1,k])+1, A[i]==B[j]
    三重循环，复杂度较高
    :param A:
    :param B:
    :return:
    """
    lenA, lenB = len(A), len(B)
    dp = [[0 for _ in range(lenB + 1)] for _ in range(lenA + 1)]
    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            if A[i - 1] != B[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                maxm = -1
                for k in range(j):
                    if B[j - 1] > B[k - 1] and dp[i - 1][k] > maxm:
                        maxm = dp[i - 1][k]
                dp[i][j] = maxm + 1
                # for k in range(j):
                #     if B[j - 1] > B[k - 1]:
                #         dp[i][j] = max(dp[i][j], dp[i - 1][k] + 1)
    return dp[-1][-1]


def lcis2(A, B):
    """
    最长上升公共子序列，即最长上升子序列+最长公共子序列
    F[i,j] = F[i-1,j], A[i]!=B[j]
           = max(F[i-1,k])+1, A[i]==B[j]
    @todo:2层循环
    :param A:
    :param B:
    :return:
    """
    lenA, lenB = len(A), len(B)
    dp = [[0 for _ in range(lenB + 1)] for _ in range(lenA + 1)]
    for i in range(1, lenA + 1):
        maxv = 1
        for j in range(1, lenB + 1):
            dp[i][j] = dp[i - 1][j]
            if A[i - 1] == B[j - 1]:
                dp[i][j] = max(dp[i][j], maxv)
            if A[i - 1] > B[j - 1]:
                maxv = max(dp[i - 1][j] + 1, maxv)
    print(dp)
    return max(dp[-1])


from typing import List


def mobileServices(cost: List[List[int]], query: List[int]) -> int:
    """
    :param cost: 从i->j的费用
    :param query: 服务
    :return:
    """
    # initial
    m, n = len(cost), len(query)
    w = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            w[i][j] = cost[i - 1][j - 1]
    p = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        p[i] = query[i - 1]
    p[0] = 3
    dp = [[[0x3f for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][1][2] = 0
    # dp
    for i in range(n):
        for x in range(1, m + 1):
            for y in range(1, m + 1):
                z = p[i]
                v = dp[i][x][y]
                if x == y or z == x or z == y:
                    continue
                u = p[i + 1]
                dp[i + 1][x][y] = min(dp[i + 1][x][y], v + w[z][u])
                dp[i + 1][z][y] = min(dp[i + 1][z][y], v + w[x][u])
                dp[i + 1][x][z] = min(dp[i + 1][x][z], v + w[y][u])
    # res
    res = float('inf')
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            z = p[n]
            if x == y or x == z or y == z:
                continue
            res = min(res, dp[n][x][y])

    return res


def differentPaths(cost):
    """
    在矩阵n*m中寻找2条路径，值最大
    :param cost: n*m
    :return:
    """
    n, m = len(cost), len(cost[0])
    g = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            g[i][j] = cost[i - 1][j - 1]
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(m + n + 1)]
    for k in range(2, m + n + 1):
        for x1 in range(max(1, k - m), min(n + 1, k)):
            for x2 in range(max(1, k - m), min(n + 1, k)):
                for a in [0, 1]:
                    for b in [0, 1]:
                        t = g[x1][k - x1]
                        if x1 != x2 or k == 2 or k == n + m:
                            t += g[x2][k - x2]
                            dp[k][x1][x2] = max(dp[k][x1][x2], dp[k - 1][x1 - a][x2 - b] + t)

    return dp[n + m][n][n]


if __name__ == "__main__":
    # k = 1
    # people = [30]
    #
    # k = 5
    # people = [1, 1, 1, 1, 1]
    # print(picturePermutations(k, people))
    #
    # k = 3
    # people = [3, 2, 1]
    # print(picturePermutations(k, people))
    #
    # k = 4
    # people = [5, 3, 3, 1]
    # print(picturePermutations(k, people))
    nums1 = [2, 2, 1, 3]
    nums2 = [2, 1, 2, 3]
    print(lcis(nums1, nums2))
    print(lcis2(nums1, nums2))

    # cost = [[0, 1, 1, 1, 1],
    #         [1, 0, 2, 3, 2],
    #         [1, 1, 0, 4, 1],
    #         [2, 1, 5, 0, 1],
    #         [4, 2, 3, 4, 0]]
    # query = [4, 2, 4, 1, 5, 4, 3, 2, 1]
    # print(mobileServices(cost, query))

    cost = [[0, 3, 9],
            [2, 8, 5],
            [5, 7, 0]]
    print(differentPaths(cost))
