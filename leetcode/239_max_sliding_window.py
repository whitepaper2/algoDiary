#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 下午4:52
# @Author  : pengyuan.li
# @Site    : 
# @File    : 239_max_sliding_window.py
# @Software: PyCharm

from typing import List
import heapq


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    out = []
    for i in range(n - k + 1):
        window = nums[i:i + k]
        if len(window) != 0:
            out.append(max(window))
    return out


def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
    """
    python heapq维护一个最小堆，数据和下标组成元组，遍历数组逐个加入，如果首元素不在窗口内，则删除，重新构造堆。
    :param nums:原始数组
    :param k:滑动窗口k
    :return:返回窗口中的最大值
    """
    if not nums: return []
    if k >= len(nums): return [max(nums)]
    heap = []
    for i in range(0, k): heapq.heappush(heap, (-nums[i], i))
    maxList = [max(nums[0:k])]
    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        while heap[0][1] <= i - k: heapq.heappop(heap)
        maxList.append(-heap[0][0])
    return maxList


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k))
    print(maxSlidingWindow2(nums, k))
