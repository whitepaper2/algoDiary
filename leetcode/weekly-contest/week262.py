#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 上午10:08
# @Author  : pengyuan.li
# @Site    : 
# @File    : week262.py
# @Software: PyCharm

"""
5897. 将数组分成两个数组并最小化数组和的差
给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。
nums 中每个元素都需要放入两个数组之一。

请你返回 最小 的数组和之差。

"""
from typing import List
from collections import defaultdict


def minimumDifference(nums: List[int]) -> int:
    """
    min(abs(s1-s2))等价于min(abs(2*s1-s))，距离最近
    :param nums:
    :return:
    """
    n = len(nums)
    idx = n // 2
    totalSum = sum(nums)
    doubleNums = [2 * x for x in nums]

    def getRangeSumSet(A, startIdx, endIdx):
        """
        得到区间[startIdx,endIdx)内cnt个元素和，返回有序集合
        :param A:
        :param cnt:
        :param startIdx:
        :param endIdx:
        :return:
        """
        setDict = defaultdict(list)
        setDict[0] = [0]
        rangeA = A[startIdx:endIdx]
        n = endIdx - startIdx
        for i in range(1, 1 << n):
            idx = bin(i).count('1')
            curSum = 0
            for j in range(n):
                if (1 << j) & i:
                    curSum += rangeA[j]
            setDict[idx].append(curSum)
        return setDict

    def twoSum(A: List[int], B: List[int], target: int):
        """
        两单调非减数列的和 与 target最近
        :param A:
        :param B:
        :param target:
        :return:
        """
        A.sort(reverse=True)
        B.sort(reverse=True)
        lenA = len(A)
        lenB = len(B)
        left = 0
        right = lenB - 1
        res = float('inf')
        while left < lenA and right > -1:
            curSum = A[left] + B[right]
            if curSum == target:
                return 0
            elif curSum > target:
                left += 1
            else:
                right -= 1
            res = min(abs(curSum - target), res)
        return res

    leftSumSet = getRangeSumSet(doubleNums, 0, idx)
    rightSumSet = getRangeSumSet(doubleNums, idx, n)
    res = float('inf')
    for i in range(idx + 1):
        left = leftSumSet[i]
        right = rightSumSet[idx - i]
        res = min(res, twoSum(left, right, totalSum))
    return res


def minimumDifference2(nums: List[int]) -> int:
    """
    状态压缩，当n<15时可以通过；>15会超时
    :param nums:
    :return:
    """
    n = len(nums)
    totalSum = sum(nums)
    res = float('inf')
    for i in range(1, 1 << n):
        if bin(i).count('1') == n // 2:
            curSum = 0
            for j in range(n):
                if (1 << j) & i:
                    curSum += nums[j]
            res = min(res, abs(2 * curSum - totalSum))
    return res


if __name__ == "__main__":
    nums = [2, -1, 0, 4, -2, -9]
    print(minimumDifference(nums))

    nums = [2, -1, 0, 4, -2, -9]
    print(minimumDifference2(nums))
