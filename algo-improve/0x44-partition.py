#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 上午10:40
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x44-partition.py
# @Software: PyCharm


import math


class Partitions(object):
    def __init__(self):
        """
        rangeSum:块的和rangeSum
        add:每个位置增加值，增量标记
        pos:{位置:块}，通过位置快速查找块
        """
        self.maxN = 100
        self.A = []
        self.rangeSum = [0] * self.maxN
        self.add = [0] * self.maxN
        self.pos = [0] * self.maxN
        self.rangeLeft = [0] * self.maxN
        self.rangeRight = [0] * self.maxN

    def build(self, nums):
        """
        初始化数组，
        分块[rangeLeft,rangeRight]
        区间和
        :param nums:
        :return:
        """
        N = len(nums)
        while self.maxN < N:
            self.maxN += self.maxN
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
                self.rangeSum[i] += self.A[j]

    def _bruteSum(self, l, r, p):
        """
        [l,r]区间和，属于位置p
        :param l:
        :param r:
        :param p:
        :return:
        """
        res = 0
        for i in range(l, r + 1):
            res += self.A[i]
        res += self.add[p] * (r - l + 1)
        return res

    def ask(self, l, r):
        """
        [l,r]区间和
        :param l:
        :param r:
        :return:
        """
        p, q = self.rangeLeft[l], self.rangeRight[r]
        res = 0
        if p == q:
            res = self._bruteSum(l, r, p)
        else:
            for i in range(p + 1, q):
                res += self.rangeSum[i] + self.add[i] * (self.rangeRight[i] - self.rangeLeft[i] + 1)
            res += self._bruteSum(l, self.rangeRight[p], p)
            res += self._bruteSum(self.rangeLeft[q], r, q)
        return res

    def _bruteChange(self, l, r, v, p):
        """
        [l,r]在位置p，增加v
        :param l:
        :param r:
        :param v:
        :param p:
        :return:
        """
        for i in range(l, r + 1):
            self.A[i] += v
        self.rangeSum[p] += v * (r - l + 1)

    def change(self, l, r, v):
        p = self.pos[l]
        q = self.pos[r]
        if p == q:
            self._bruteChange(l, r, v, p)
        else:
            for i in range(p + 1, q):
                self.add[i] += v

            lp, rp = self.rangeLeft[p], self.rangeRight[p]
            self._bruteChange(lp, rp, v, p)

            lq, rq = self.rangeLeft[q], self.rangeRight[q]
            self._bruteChange(lq, rq, v, q)


def tinyProblemByPartition(nums, commands):
    """
    通过分块方法解决区间和问题
    :param nums:
    :param commands:
    :return:
    """
    pp = Partitions()
    pp.build(nums)
    for command in commands:
        if command[0] == 'Q':
            left, right = command[1], command[2]
            res = pp.ask(left, right)
            print("[{},{}]-Sum={}".format(left, right, res))
        else:
            left, right, v = command[1], command[2], command[3]
            pp.change(left, right, v)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    commands = [['Q', 4, 4], ['Q', 1, 10], ['Q', 2, 4], ['C', 3, 6, 3], ['Q', 2, 4]]
    tinyProblemByPartition(nums, commands)
