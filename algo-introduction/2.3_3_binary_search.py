#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm


def subSearch(A, left, right, x):
    if left < right:
        mid = (left + right) // 2
        if A[mid] == x:
            return mid
        l1 = subSearch(A, left, mid, x)
        if l1 != -1:
            return l1
        r1 = subSearch(A, mid + 1, right, x)
        if r1 != -1:
            return r1

    return -1


def recursiveBinSearch(nums, x):
    """
    已排序，递归查找x
    :param nums:
    :param x:
    :return:
    """
    ind = subSearch(nums, 0, len(nums) - 1, x)
    return ind


def iterBinSearch(nums, x):
    """
    已排序，循环查找x
    :param nums:
    :param x:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    nums = [26, 31, 41, 41, 58, 59]
    x = 58
    print(recursiveBinSearch(nums, x))
    print(iterBinSearch(nums, x))
