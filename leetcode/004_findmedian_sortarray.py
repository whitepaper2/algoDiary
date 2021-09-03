#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 下午3:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 004_findmedian_sortarray.py
# @Software: PyCharm
import sys
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    if m == 0:
        if n % 2 == 0:
            return (nums2[n // 2] + nums2[n // 2 - 1]) / 2
        else:
            return nums2[n // 2]
    if n == 0:
        if m % 2 == 0:
            return (nums1[m // 2] + nums1[m // 2 - 1]) / 2
        else:
            return nums1[m // 2]
    mid = (m + n) // 2
    nums1_2 = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums1_2.append(nums1[i])
            i = i + 1
        elif nums1[i] > nums2[j]:
            nums1_2.append(nums2[j])
            j = j + 1
        else:
            nums1_2.append(nums1[i])
            nums1_2.append(nums2[j])
            i = i + 1
            j = j + 1
    if i == m:
        while j < n:
            nums1_2.append(nums2[j])
            j = j + 1
    if j == n:
        while i < m:
            nums1_2.append(nums1[i])
            i = i + 1
    if (m + n) % 2 == 0:
        return (nums1_2[mid] + nums1_2[mid - 1]) / 2
    else:
        return nums1_2[mid]


def findMedianSortedArrays2(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    left = (m + n + 1) // 2
    right = (m + n + 2) // 2
    return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right)) / 2


def findKth(nums1, i, nums2, j, k):
    if i >= len(nums1):
        return nums2[j + k - 1]
    if j >= len(nums2):
        return nums1[i + k - 1]
    if k == 1:
        return min(nums1[i], nums2[j])
    midval1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else sys.maxsize
    midval2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else sys.maxsize
    if midval1 < midval2:
        return findKth(nums1, i + k // 2, nums2, j, k - k // 2)
    else:
        return findKth(nums2, i, nums2, j + k // 2, k - k // 2)


def find_median(nums: List[int]) -> float:
    """
    寻找有序数组的中位数，个数n=奇数，中位数=中间一个数，(n+1)/2 == (n+2)/2；个数n=偶数，中位数=中间两个数，(n+1)/2 and (n+2)/2
    :param nums: 原数组
    :return: 中位数
    """
    if nums is None:
        return -1.0
    n = len(nums)
    if n == 0:
        return -1.0
    median = (nums[(n + 1) // 2 - 1] + nums[(n + 2) // 2 - 1]) / 2
    return median


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))
    print(findMedianSortedArrays2(nums1, nums2))

    nums = [1, 3, 5, 7, 8, 10]
    print(find_median(nums))

    nums = [1, 3, 5, 7, 8]
    print(find_median(nums))
