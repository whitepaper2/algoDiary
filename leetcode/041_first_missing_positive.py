#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 下午5:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : 039_combination_sum.py
# @Software: PyCharm


from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    """
    note: 返回第一个缺失的正值。遍历数据，若A[i]<n and A[i]!=i+1，则交换A[i]与A[A[i]-1]
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(n):
        if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            swap2(nums[nums[i] - 1], nums[i])
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1


def swap2(num1, num2):
    tmp = num1
    num1 = num2
    num2 = tmp
    return num1, num2


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    print(firstMissingPositive(candidates))

    candidates = [2, 3, 5]
    print(firstMissingPositive(candidates))
