#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 下午3:39
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x44-onlineMode.py
# @Software: PyCharm

import math
from collections import Counter, defaultdict


class RangeMode(object):
    def __init__(self):
        self.A = []
        self.maxN = 100
        self.pos = [0] * self.maxN
        self.rangeLeft = [0] * self.maxN
        self.rangeRight = [0] * self.maxN
        self.mode = [[0 for _ in range(self.maxN)] for _ in range(self.maxN)]

    def _buildRange(self, psize, x):
        ct = {x: 0 for x in list(set(self.A))}
        mx = -1
        res = 0

        for j in range(x, psize + 1):
            for i in range(self.rangeLeft[j], self.rangeRight[j] + 1):
                ct[self.A[i]] += 1
                if ct[self.A[i]] > mx or (ct[self.A[i]] == mx and self.A[i] < res):
                    res = self.A[i]
                    mx = ct[self.A[i]]
            self.mode[x][j] = res

    def build(self, nums):
        N = len(nums)
        self.A = [0] + nums
        psize = int(math.sqrt(N))
        for i in range(1, psize + 1):
            self.rangeLeft[i] = (i - 1) * psize + 1
            self.rangeRight[i] = i * psize
        if self.rangeRight[psize] < N:
            psize += 1
            self.rangeLeft[psize] = self.rangeRight[psize - 1] + 1
            self.rangeRight[psize] = N
        for i in range(1, psize + 1):
            for j in range(self.rangeLeft[i], self.rangeRight[i] + 1):
                self.pos[j] = i
            self._buildRange(psize, i)

    def ask(self, l, r):
        p, q = self.pos[l], self.pos[r]
        if p == q:
            return self.mode[p][p]
        else:
            # @todo:跨区域的众数
            res = self.mode[p + 1][q - 1]
        return res


def rangeMode(A, commands):
    """
    初始化每个区间的众数
    :param A:
    :param commands:
    :return:
    """
    N = len(A)
    uniq = defaultdict(list)
    for i, v in enumerate(A):
        uniq[v].append(i + 1)
    A.insert(0, 0)
    maxN = 100
    psize = int(math.sqrt(N))
    rangeLeft = [0] * maxN
    rangeRight = [0] * maxN
    rangeMode = [0] * maxN
    pos = [0] * maxN
    for i in range(1, psize + 1):
        rangeLeft[i] = (i - 1) * psize + 1
        rangeRight[i] = i * psize
    if rangeRight[psize] < N:
        psize += 1
        rangeLeft[psize] = rangeRight[psize - 1] + 1
        rangeRight[psize] = N
    for i in range(1, psize + 1):
        cntDict = Counter(A[rangeLeft[i]:rangeRight[i] + 1])
        maxCnt = max([v for k, v in cntDict.items()])
        ks = []
        for k, v in cntDict.items():
            if v == maxCnt:
                ks.append(k)
        rangeMode[i] = ks
        for j in range(rangeLeft[i], rangeRight[i] + 1):
            pos[j] = i

    for l, r in commands:
        p, q = pos[l], pos[r]
        if p == q:
            for i in range(l, r + 1):
                if A[i] in rangeMode[p]:
                    return A[i]
        else:

            pass
        pass
    pass


if __name__ == "__main__":
    nums = [1, 4, 2, 3, 2, 4, 3, 2, 1, 4]
    om = RangeMode()
    om.build(nums)
    print(om.mode)
    print(om.pos)
    commands = [[1, 2], [3, 8]]
    rangeMode(nums, commands)
