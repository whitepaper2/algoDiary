#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 上午8:52
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x12-monotoQueue.py
# @Software: PyCharm

from itertools import accumulate


def monotoSum(nums, m):
    """
    求一段长度不超过m连续数组和
    :param nums:
    :param m:
    :return:
    """
    preSum = list(accumulate(nums))  # 前缀和
    n = len(nums)
    left, right = 1, 1
    preSum.insert(0, 0)
    res = float('-inf')
    queue = [0] * (n + 1)  # 存储下标
    for i in range(1, n + 1):
        while left <= right and i - queue[left] > m:
            left += 1
        res = max(res, preSum[i] - preSum[queue[left]])
        while left <= right and preSum[queue[right]] >= preSum[i]:
            right -= 1
        right += 1
        queue[right] = i
    return res


if __name__ == "__main__":
    nums = [1, -3, 5, 1, -2, 3]
    m = 4
    print(monotoSum(nums, m))
