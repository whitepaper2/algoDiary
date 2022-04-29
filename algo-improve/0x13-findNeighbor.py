#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 下午4:12
# @Author  : pengyuan.li
# @Site    :
# @File    : 0x13-findNeighbor.py
# @Software: PyCharm

from sortedcontainers import SortedList


def findNeighbor(nums):
    """
    nums互不相同
    返回[2,n]，使得min(abs(A[i]-A[j])), j<i,
    :param nums:
    :return:j, minj
    """
    res = []
    n = len(nums)
    nums.insert(0, float('-inf'))
    v2id = {}

    for i, e in enumerate(nums):
        v2id[e] = i

    sortsets = SortedList()
    sortsets.append(nums[1])
    for i in range(2, n + 1):
        sortsets.add(nums[i])
        idx = sortsets.bisect_left(nums[i])
        cur = float('inf')
        j = i

        if idx - 1 >= 0:
            t = abs(nums[i] - sortsets[idx - 1])
            if cur > t:
                cur = t
                j = v2id[sortsets[idx - 1]]
        if idx + 1 < len(sortsets):
            t = abs(nums[i] - sortsets[idx + 1])
            if cur > t:
                cur = t
                j = v2id[sortsets[idx + 1]]
        res.append([j, cur])
    return res


if __name__ == "__main__":
    nums = [1, 5, 3]
    print(findNeighbor(nums))
