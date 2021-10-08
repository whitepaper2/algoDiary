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
    cnts = 0
    n1 = q - p + 1
    n2 = r - q
    L = [A[p + i] for i in range(0, n1)]
    L.append(float("inf"))
    R = [A[q + 1 + i] for i in range(0, n2)]
    R.append(float("inf"))
    k = p
    i, j = 0, 0
    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            cnts += n1-i
            A[k] = R[j]
            j += 1
        k += 1
    return cnts


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


def subInversePair(A, p, q):
    if p < q:
        mid = (p + q) // 2
        left = subInversePair(A, p, mid)
        right = subInversePair(A, mid + 1, q)
        return left + right + merge(A, p, mid, q)
    return 0


def divideInversePair(nums):
    """
    note: 算法导论-2.1-2练习题：选择排序，非升序。分治法
    :param nums: List[Int]
    :return: List[Int]
    """

    return subInversePair(nums, 0, len(nums) - 1)


def bruteInversePair(A):
    """
    求数组中的逆序对，2层遍历
    :param A:
    :return:
    """
    cnts = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                cnts += 1
    return cnts


if __name__ == "__main__":
    nums = [31, 41, 59, 26, 41, 58]
    print(bruteInversePair(nums))
    print(divideInversePair(nums))
