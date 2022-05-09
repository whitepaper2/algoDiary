#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/05/06 11:23:36
@Author  : pengyuan.li
@File    : 0x14-hash.py
@Software: VSCode
'''

# here put the import lib
from collections import defaultdict
from typing import List


def findSameSnow(n, snow: List[List[int]]) -> bool:
    hashVal = defaultdict(list)
    idx = 0

    def insert(A: List[int]) -> bool:
        nonlocal idx
        v = calcHash(A)
        if hashVal.get(v):
            for i in hashVal.get(v):
                if isEqualSnow(snow[i], A):
                    return True
        hashVal[v].append(idx)
        idx += 1
        return False

    def calcHash(A: List[int]) -> int:
        P = 99991
        s, m = 0, 1
        for v in A:
            s = (s + v) % P
            m = (m * v) % P
        return (s + m) % P

    def isEqualSnow(p: List[int], q: List[int]) -> bool:
        psize = 6
        for i in range(psize):
            for j in range(psize):
                # 顺时针
                isEqual = 1
                for k in range(psize):
                    if p[(i + k) % psize] != q[(j + k) % psize]:
                        isEqual = 0
                if isEqual:
                    return True
                # 逆时针
                isEqual = 1
                for k in range(psize):
                    if p[(i + k) % psize] != q[(j - k + psize) % psize]:
                        isEqual = 0
                if isEqual:
                    return True
        return False

    for i in range(n):
        if insert(snow[i]):
            return True
    return False


if __name__ == "__main__":
    n = 2
    snow = [[1, 2, 3, 4, 5, 6], [4, 3, 2, 1, 6, 5]]
    print(findSameSnow(n, snow))
