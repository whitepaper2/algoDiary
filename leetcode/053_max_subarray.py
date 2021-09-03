#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 下午9:26
# @Author  : pengyuan.li
# @Site    : 
# @File    : 053_max_subarray.py
# @Software: PyCharm
from common import timeit


@timeit
def max_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    out = -float('inf')
    dp = 0
    for i in range(len_nums):
        dp = max(dp + nums[i], nums[i])
        out = max(dp, out)
    return out


@timeit
def max_subarray2(nums):
    """
    note:分治法，在合并时使用动态规划，cost time = 分治法 + 动态规划
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    left = 0
    right = len_nums - 1

    def get_maximum(nums, left, right):
        if left >= right:
            return nums[left]
        middle = int((left + right) / 2)
        lmax = get_maximum(nums, left, middle - 1)
        rmax = get_maximum(nums, middle + 1, right)
        mmax = -float("inf")
        dp = 0
        for i in range(left, right + 1):
            dp = max(dp + nums[i], nums[i])
            mmax = max(dp, mmax)
        mmax = max(mmax, lmax, rmax)
        return mmax

    out = get_maximum(nums, left, right)
    return out


@timeit
def max_subarray3(nums):
    """
    note: 分治法，1、最大值在左边；2、最大值在右边；3、最大值必须经过mid点
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    left = 0
    right = len_nums - 1

    def get_maximum(nums, left, right):
        if left >= right:
            return nums[left]
        middle = int((left + right) / 2)
        lmax = get_maximum(nums, left, middle - 1)
        rmax = get_maximum(nums, middle + 1, right)
        mmax = nums[middle]
        t = mmax
        for i in range(middle-1, left-1, -1):
            t = t + nums[i]
            mmax = max(t, mmax)
        t = mmax
        for i in range(middle+1, right+1):
            t = t + nums[i]
            mmax = max(t, mmax)
        mmax = max(mmax, lmax, rmax)
        return mmax

    out = get_maximum(nums, left, right)
    return out


if __name__ == "__main__":
    """
    note: Given List[int], find the continous subarray which has the largest sum, out=sum
    """
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray2(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray3(nums))
