#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/11 17:45:13
@Author  : pengyuan.li
@File    : 0x03-prefixSum.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def maxBomb(A: List[List[int]], r: int) -> int:
    """
    一颗炸弹在区域r内能获得最大价值
    :param: A:List[List[int]]
    :param: r:int
    :return:
    """
    m, n = len(A), len(A[0])
    preSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            preSum[i + 1][j + 1] = preSum[i + 1][j] + preSum[i][
                j + 1] - preSum[i][j] + A[i][j]
    res = 0
    for i in range(m):
        for j in range(n):
            leftx, lefty = max(1, i - r + 1), max(1, j - r + 1)
            res = max(
                res, preSum[i + 1][j + 1] - preSum[i + 1][lefty] -
                preSum[leftx][j + 1] + preSum[leftx][lefty])
    return res


def incdecNum(A: List[int]) -> int:
    """
    给定一组数，op:在区间[l,r]中所有数增加1或减少1，求使得数组取得相同数最少的op
    return:最少操作次数，以及在最少操作次数下得到几个不同的数列
    note:差分数列b，b[1]=a[1],b[i]=a[i]-a[i-1]（2<=i<=n）,b[n+1]=0
    1.2<=i<=n,任取两个b[i],b[j],一个+1，一个-1
    2.b[1]与b[i]（2<=i<=n）匹配
    3.b[n+1]与b[i]（2<=i<=n）匹配
    4.b[1]与b[n+1]匹配，无意义
    """
    n = len(A)
    B = [0] * (n + 1)
    B[0] = A[0]
    for i in range(1, n):
        B[i] = A[i] - A[i - 1]
    p, q = 0, 0
    for i in range(1, n):
        if B[i] > 0:
            p += 1
        if B[i] < 0:
            q += 1
    minOP = max(p, q)
    res = abs(p - q) + 1
    return minOP, res


def tallestCow(N, P, H, relations):
    """
    一排牛站成一队，当两头牛比他们中间位置牛高时，两头牛相互可以看见，求每头牛最大可能高度。
    N:牛的总数
    P:最高的牛所在位置
    H:最高的牛的高度
    relations:相互可以看见的两头牛位置
    """
    dupRelations = []
    for a, b in relations:
        if a > b:
            a, b = b, a
        if [a, b] not in dupRelations:
            dupRelations.append([a, b])
    C = [0] * (N + 1)
    # 复杂度 O(mn)
    for a, b in dupRelations:
        for i in range(a + 1, b):
            C[i] -= 1
    h = 0
    if C[P] > 0:
        h = -C[P]
    if C[P] < 0:
        h = C[P]

    for i in range(1, N + 1):
        C[i] += H + h
    return C[1:]


def tallestCow2(N, P, H, relations):
    """
    一排牛站成一队，当两头牛比他们中间位置牛高时，两头牛相互可以看见，求每头牛最大可能高度。
    N:牛的总数
    P:最高的牛所在位置
    H:最高的牛的高度
    relations:相互可以看见的两头牛位置
    """
    dupRelations = []
    for a, b in relations:
        if a > b:
            a, b = b, a
        if [a, b] not in dupRelations:
            dupRelations.append([a, b])
    C = [0] * (N + 1)
    d = [0] * (N + 1)
    # 复杂度 O(mn)
    for a, b in dupRelations:
        d[a + 1] -= 1
        d[b] += 1
    res = []
    for i in range(1, N + 1):
        C[i] = C[i - 1] + d[i]
        res.append(C[i]+H)
    return res


if __name__ == "__main__":
    mat = [[0, 0, 1], [1, 1, 1]]
    r = 1
    print(maxBomb(mat, r))

    nums = [1, 1, 2, 2]
    print(incdecNum(nums))

    N = 9
    P = 3
    H = 5
    relations = [[1, 3], [5, 3], [4, 3], [3, 7], [9, 8]]
    print(tallestCow(N, P, H, relations))
    print(tallestCow2(N, P, H, relations))
