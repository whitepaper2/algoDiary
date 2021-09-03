#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm


def merge(A, p, q, r):
    """
    note：排序有序数组，哨兵，复制出来，重新构造，双指针
    :param A:
    :param p:
    :param q:
    :param r:
    :return:
    """
    n1 = q - p + 1
    n2 = r - q
    L = [A[p + i] for i in range(0, n1)]
    L.append(float("inf"))
    R = [A[q + 1 + i] for i in range(0, n2)]
    R.append(float("inf"))
    k = p
    i, j = 0, 0
    while k <= r:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


def merge2(A, p, q, r):
    """
    note：排序有序数组，复制出来，重新构造，双指针
    :param A:
    :param p:
    :param q:
    :param r:
    :return:
    """
    n1 = q - p + 1
    n2 = r - q
    L = [A[p + i] for i in range(0, n1)]
    R = [A[q + 1 + i] for i in range(0, n2)]
    k = p
    i, j = 0, 0
    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    if i == n1:
        while j < n2:
            A[k] = R[j]
            k += 1
            j += 1
    if j == n2:
        while i < n1:
            A[k] = L[i]
            k += 1
            i += 1


def subMerge(A, p, q):
    if p < q:
        mid = (p + q) // 2
        subMerge(A, p, mid)
        subMerge(A, mid + 1, q)
        merge2(A, p, mid, q)


def merge_sort(nums):
    """
    note: 算法导论-2.1-2练习题：选择排序，非升序。分治法
    :param nums: List[Int]
    :return: List[Int]
    """
    subMerge(nums, 0, len(nums) - 1)
    return nums


if __name__ == "__main__":
    nums = [31, 41, 59, 26, 41, 58]
    print(merge_sort(nums))
