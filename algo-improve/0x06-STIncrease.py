#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 上午10:36
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x06-STIncrease.py
# @Software: PyCharm

"""
ST(sparse table)，是一种利用倍增的方式求区间的最值问题，当然也可以求满足结合律的问题
可重复区间 也可以进行信息合并
"""

import math


class STMax(object):
    def __init__(self, nums):
        self.A = nums
        self.length = len(self.A)
        self.maxN = 20
        self.logN = dict()
        # 1.预处理log
        for i in range(2, self.maxN):
            self.logN[i] = int(math.log2(i / 2)) + 1
        # 2.预处理区间最大值
        self.f = [[0] * self.maxN for _ in range(self.maxN)]
        for i in range(self.length):
            self.f[i][0] = self.A[i]
        for i in range(1, self.length):
            j = 1
            while j + (1 << (i - 1)) < self.length:
                self.f[j][i] = max(self.f[j][i - 1], self.f[j + (1 << (i - 1))][i - 1])
                j += 1

    def query(self, left, right):
        """
        得到区间[left,right]的最大值
        :param left:
        :param right:
        :return:
        """
        if not 0 <= left <= right < self.length:
            raise Exception("please input parameter again!")

        # 2.查询区间的最值
        s = self.logN[right - left + 1]
        return max(self.f[left][s], self.f[right - (1 << s) + 1][s])


if __name__ == "__main__":
    nums = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    st = STMax(nums)
    print(st.query(3, 8))
