#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/20 10:07:46
@Author  : pengyuan.li
@File    : 0x02-recursion.py
@Software: VSCode
'''

# here put the import lib
import re


def allSubset(n):
    """
    note:输出1-n的所有子集
    位运算遍历所有子集
    """
    res = []
    nums = list(range(1, n + 1))
    for i in range(1 << n):
        cur = []
        for k in range(n):
            if (i >> k) & 1:
                cur.append(nums[k])
        res.append(list(cur))
    # print(len(res))
    return res


def allSubset2(n):
    """
    note:输出1-n的所有子集
    递归计算
    """
    nums = list(range(1, n + 1))
    res = []
    chosen = [0] * n

    def calc(i):
        if i == n:
            res.append([nums[i] for i, x in enumerate(chosen) if x == 1])
            return
        # 不选择 i
        calc(i + 1)
        # 选择 i
        chosen[i] = 1
        calc(i + 1)
        chosen[i] = 0  # 还原现场

    calc(0)
    # print(len(res))
    return res


def partSubset(n, m):
    """
    note:输出1-n的长度为m的子集
    递归计算
    """
    nums = list(range(1, n + 1))
    if m >= n:
        return [nums]
    res = []
    chosen = [0] * n

    def calc(i):
        # 剪枝，删除长度大于m的子集
        if i > n or sum(chosen) > m:
            return
        # print(sum(chosen))
        if i == n:
            if sum(chosen) == m:
                res.append([nums[i] for i, x in enumerate(chosen) if x == 1])
            return
        # 不选择 i
        calc(i + 1)
        # 选择 i
        chosen[i] = 1
        calc(i + 1)
        chosen[i] = 0  # 还原现场

    calc(0)
    # print(len(res))
    return res


if __name__ == "__main__":
    n = 5
    print(allSubset(n))
    print(allSubset2(n))
    print(partSubset(n, 3))
