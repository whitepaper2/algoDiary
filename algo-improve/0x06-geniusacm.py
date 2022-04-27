#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/27 16:54:20
@Author  : pengyuan.li
@File    : 0x06-geniusacm.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def geniusAcm(A: List[int], M: int, T: int) -> int:
    """
    我们要把 A 分成若干段，M对数(2*M)，使得每一段的“校验值”都不超过 T。
    求最少需要分成几段。
    """
    res = 0
    start = 0
    n = len(A)

    def getSqrt(l, r):
        tmpList = []
        for i in range(l, r + 1):
            tmpList.append(A[i])
        tmpList.sort()
        k = len(tmpList)
        s = 0
        for i in range(min(M, k)):
            s += (tmpList[k - 1] - tmpList[i]) * (tmpList[k - 1] - tmpList[i])
            k -= 1
        return s

    while start < n:
        l = start
        r = n
        while l < r:
            mid = (l + r) >> 1
            if getSqrt(start, mid) > T:
                r = mid
            else:
                l = mid + 1
        start = r
        res += 1
    return res


def geniusAcm2(A: List[int], M: int, T: int) -> int:
    """
    我们要把 A 分成若干段，M对数(2*M)，使得每一段的“校验值”都不超过 T。
    求最少需要分成几段。
    """
    res = 0
    n = len(A)

    def getSqrt(l, r):
        tmpList = []
        for i in range(l, r):
            tmpList.append(A[i])
        tmpList.sort()
        k = len(tmpList)
        s = 0
        for i in range(min(M, k)):
            s += (tmpList[k - 1] - tmpList[i]) * (tmpList[k - 1] - tmpList[i])
            k -= 1
        return s

    l, r = 0, 0
    while r < n:
        p = 1
        while p > 0:
            # [l,r+p)
            if r + p <= n and getSqrt(l, r + p) <= T:
                r += p
                p <<= 1
            else:
                p >>= 1
        l = r
        res += 1
    return res


if __name__ == "__main__":
    A = [8, 2, 1, 7, 9]
    M = 1
    T = 49
    print(geniusAcm(A, M, T))
    print(geniusAcm2(A, M, T))

    A = [8, 2, 1, 7, 9]
    M = 1
    T = 64
    print(geniusAcm(A, M, T))
    print(geniusAcm2(A, M, T))
