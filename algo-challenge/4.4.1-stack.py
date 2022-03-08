#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/03 13:49:02
@Author  : pengyuan.li
@File    : 4.4.1-stack.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def maxRectangle(heights: List[int]) -> int:
    """
    最大矩阵，[L,R]高度h，小于L or 大于R的高度都小于h
    """
    n = len(heights)
    pq = [0] * n
    left, right = [0] * n, [0] * n
    t = 0
    for i, h in enumerate(heights):
        while t > 0 and heights[pq[t - 1]] >= h:
            t -= 1
        if t == 0:
            left[i] = 0
        else:
            left[i] = pq[t - 1] + 1
        pq[t] = i
        t += 1

    t = 0
    for i in range(n - 1, -1, -1):
        while t > 0 and heights[pq[t - 1]] >= heights[i]:
            t -= 1
        if t == 0:
            right[i] = n
        else:
            right[i] = pq[t - 1]
        pq[t] = i
        t += 1
    res = 0
    for i in range(n):
        res = max(res, heights[i] * (right[i] - left[i]))
    # print(left)
    # print(right)
    return res


import heapq


def rangeMinimum(nums: List[int], k: int) -> List[int]:
    if len(nums) <= k:
        return [min(nums)]
    pq = [(nums[i], i) for i in range(k)]
    heapq.heapify(pq)
    res = [pq[0][0]]
    for i in range(k, len(nums)):
        heapq.heappush(pq, (nums[i], i))
        while pq and pq[0][1] <= i - k:
            heapq.heappop(pq)
        res.append(pq[0][0])

    return res


if __name__ == "__main__":
    # heights = [2, 1, 4, 5, 1, 3, 3]
    # print(maxRectangle(heights))

    k = 3
    nums = [1, 3, 5, 4, 2]
    print(rangeMinimum(nums, k))
