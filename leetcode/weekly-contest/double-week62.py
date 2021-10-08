#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/7 下午9:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : double-week62.py
# @Software: PyCharm
"""
2025. 分割数组的最多方案数

给你一个下标从 0 开始且长度为 n 的整数数组 nums 。分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目：
1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。

请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。

"""
from typing import List


def waysToPartition(nums: List[int], k: int) -> int:
    """
    暴力解法，时间复杂度：O(n*n)
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    prefixSum = [0] * (n + 1)
    res = 0
    for i in range(1, n + 1):
        prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
    for i in range(1, n):
        if 2 * prefixSum[i] == prefixSum[n]:
            res += 1
    for i in range(n):
        cur = 0
        tmpSum = prefixSum[:i + 1]

        j = i + 1
        while j < n + 1:
            tmpSum.append(prefixSum[j] + k - nums[i])
            j += 1
        for p in range(1, n):
            if 2 * tmpSum[p] == tmpSum[-1]:
                cur += 1
        res = max(res, cur)
    return res


from collections import defaultdict


def waysToPartition2(nums: List[int], k: int) -> int:
    """
    字典存储每个和的个数
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    prefixSum = [0] * (n + 1)
    res = 0
    sumDict = defaultdict(int)
    for i in range(1, n + 1):
        prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        if i != n:
            sumDict[prefixSum[i]] += 1

    if prefixSum[n] % 2 == 0:
        res = sumDict[int(prefixSum[n] // 2)]
    for i in range(n):
        cur = 0
        sumDict = defaultdict(int)
        tmpSum = prefixSum[:i + 1]
        for p in range(1, i + 1):
            sumDict[tmpSum[p]] += 1
        j = i + 1
        while j < n + 1:
            tmpSum.append(prefixSum[j] + k - nums[i])
            if j != n:
                sumDict[tmpSum[j]] += 1
            j += 1
        if tmpSum[n] % 2 == 0:
            cur = sumDict[int(tmpSum[n] // 2)]
        res = max(res, cur)
    return res


from itertools import accumulate
from collections import Counter


def waysToPartition3(nums: List[int], k: int) -> int:
    """
    前缀和，当改变nums[i]时，presum[0:i-1]不变，presum[i:n-1]每个都+(k-nums[i])，分别维护两个指针，left\right
    随着i的改变，left\right相应的加、减
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    prefixSum = list(accumulate(nums))
    totalSum = prefixSum[n - 1]
    left = defaultdict(int)
    right = Counter(prefixSum[:n - 1])
    res = right[totalSum / 2]
    for i in range(n):
        if i > 0:
            left[prefixSum[i - 1]] += 1
            right[prefixSum[i - 1]] -= 1
        leftx = (totalSum + k - nums[i]) / 2
        rightx = totalSum / 2 - (k - nums[i]) / 2
        res = max(res, left[leftx] + right[rightx])
    return res


"""
2023. 连接后等于目标字符串的字符串对

给你一个 数字 字符串数组 nums 和一个 数字 字符串 target ，请你返回 nums[i] + nums[j] （两个字符串连接）结果等于 target 的下标 (i, j) 
（需满足 i != j）的数目。

"""


def numOfPairs(nums, target: str) -> int:
    """
    正确解法：哈希+遍历
    不正确解法：排序+二分查找，因为不具备有序性
    :param nums:
    :param target:
    :return:
    """
    strDict = dict()
    res = 0
    for s in nums:
        for k, v in strDict.items():
            if s + k == target:
                res += v
            if k + s == target:
                res += v
        if s in strDict:
            strDict[s] += 1
        else:
            strDict[s] = 1
    return res


if __name__ == "__main__":
    # nums = [2, -1, 2]
    # k = 3
    # print(waysToPartition3(nums, k))

    # nums = [0, 0, 0]
    # k = 1
    # print(waysToPartition2(nums, k))
    #
    # nums = [22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14]
    # k = -33
    # print(waysToPartition3(nums, k))
    #
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k = 0
    print(waysToPartition3(nums, k))

    # nums = ["777", "7", "77", "77"]
    # target = "7777"
    # print(numOfPairs(nums, target))
    #
    # nums = ["123", "4", "12", "34"]
    # target = "1234"
    # print(numOfPairs(nums, target))
    #
    # nums = ["1", "1", "1"]
    # target = "11"
    # print(numOfPairs(nums, target))
    #
    # nums = ["74", "1", "67", "1", "74"]
    # target = "174"
    # print(numOfPairs(nums, target))
