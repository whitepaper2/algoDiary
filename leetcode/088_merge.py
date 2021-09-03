#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 下午2:24
# @Author  : pengyuan.li
# @Site    : 
# @File    : 088_merge.py
# @Software: PyCharm


def merge(nums1, m, nums2, n):
    """
    note: 遍历nums1, 如果nums1[i]>nums2[j]，nums1向后移动一个位置，把nums2[j]放在i位置处，如果nums2还有元素，追加到nums1
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while i < m + n and j < n:
        if nums1[i] > nums2[j]:
            for k in range(m + n - 1, i, -1):
                nums1[k] = nums1[k - 1]
            nums1[i] = nums2[j]
            j = j + 1
        i = i + 1
    k = n - 1
    mk = m + n - 1
    while k >= j:
        nums1[mk] = nums2[k]
        mk = mk - 1
        k = k - 1


def merge2(nums1, m, nums2, n):
    """
    note: 从后向前遍历nums1,nums2 如果nums1[i]>nums2[j]，nums1[i]放在i+j+1位置，否则把nums2[j]放在i+j+1位置处，这样不用移动元素，节约时间
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[i + j + 1] = nums1[i]
            i = i - 1
        else:
            nums1[i + j + 1] = nums2[j]
            j = j - 1
    if j >= 0:
        nums1[:j + 1] = nums2[:j + 1]


def merge3(nums1, m, nums2, n):
    """
    note: 从后向前遍历nums1,nums2 如果nums1[i]>nums2[j]，nums1[i]放在i+j+1位置，否则把nums2[j]放在i+j+1位置处，这样不用移动元素，节约时间
    比方法2运行时间短，主要是因为比较次数少了？
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m + n - 1] = nums1[m-1]
            m = m - 1
        else:
            nums1[m + n - 1] = nums2[n-1]
            n = n - 1
    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == "__main__":
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    merge3(nums1, m, nums2, n)
    print(nums1)
    nums1 = [0]
    m = 0
    nums2 = [2]
    n = 1
    merge2(nums1, m, nums2, n)
    print(nums1)
