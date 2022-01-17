#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/12 17:05:20
@Author  : pengyuan.li
@File    : 3.2.1-sidingWindow.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def windowMaxVals(A: List[int], k: int) -> List[int]:
    # 暴力解法,求数组A中范围k的最大值
    n = len(A)
    res = []
    s = 0
    while s + k <= n:
        res.append(max(A[s:s + k]))
        s += 1
    return res


def minLength(A: List[int], S: int) -> int:
    # 总和不小于s的连续子序列和
    s, t, n = 0, 0, len(A)
    res = n + 1
    psum = 0
    while True:
        while t < n and psum < S:
            psum += A[t]
            t += 1
        if t == n:
            break
        res = min(res, t - s)
        if s < n:
            psum -= A[s]
            s += 1
    if res > n:
        return 0
    return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # [3, 3, 5, 5, 6, 7]
    print(windowMaxVals(nums, k))

    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    s = 15
    print(minLength(nums, s))
