#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 下午8:42
# @Author  : pengyuan.li
# @Site    : 
# @File    : 003_merge_sort.py
# @Software: PyCharm
from typing import List


def merge_nums(nums, start1, end1, start2, end2):
    """
    合并两个有序数组
    :param nums:
    :param start1:
    :param end1:
    :param start2:
    :param end2:
    :return:
    """
    n = (end1 - start1 + 1) + (end2 - start2 + 1)
    tmp = [0] * n
    i = start1
    j = start2
    k = 0
    while i <= end1 and j <= end2:
        if nums[i] > nums[j]:
            tmp[k] = nums[j]
            j = j + 1
        else:
            tmp[k] = nums[i]
            i = i + 1
        k = k + 1
    while i <= end1:
        tmp[k] = nums[i]
        k = k + 1
        i = i + 1
    while j <= end2:
        tmp[k] = nums[j]
        k = k + 1
        j = j + 1
    nums[start1:start1 + n] = tmp


def merge_sort(nums: List[int]):
    """
    note:归并排序算法，自顶向下，递归计算
    :param nums:
    :return:
    """
    n = len(nums)

    def sub_merge_sort(nums, start, end):
        if start < end:
            mid = (start + end) // 2
            sub_merge_sort(nums, start, mid)
            sub_merge_sort(nums, mid + 1, end)
            merge_nums(nums, start, mid, mid + 1, end)

    sub_merge_sort(nums, 0, n - 1)


def merge_sort2(nums: List[int]):
    """
    note:归并排序算法，自下向上
    :param nums:
    :return:
    """
    n = len(nums)
    after_size = 1
    while after_size < n:
        before_size = after_size
        after_size = 2 * before_size
        i = 0
        while i + after_size < n:
            merge_nums(nums, i, i + before_size, i + before_size + 1, i + after_size)
            i = i + after_size
        if i + before_size < n:
            merge_nums(nums, i, i + before_size, i + before_size + 1, n - 1)


if __name__ == "__main__":
    nums = [8, 5, 3, 9, 11, 6, 4, 1, 10, 7, 2]
    merge_sort(nums)
    print(nums)
    merge_sort2(nums)
    print(nums)
    nums = [3, 9, 11, 4, 7]
    merge_nums(nums, 0, 2, 3, 4)
    print(nums)
