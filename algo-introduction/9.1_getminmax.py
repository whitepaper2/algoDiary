#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午9:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 005_is_heap.py
# @Software: PyCharm


def getMinMax(A):
    minVal = float("inf")
    maxVal = float("-inf")
    i, j = 0, len(A) - 1
    while i <= j:
        maxij = max(A[i], A[j])
        minij = min(A[i], A[j])
        if maxij > maxVal:
            maxVal = maxij
        if minij < minVal:
            minVal = minij
        i += 1
        j -= 1
    return minVal, maxVal


import random


def randomPartition(A, p, r):
    """
    返回枢纽点q，在q之前的都小于A[q]，之后的都大于A[q]
    :param A:
    :param p:
    :param r:
    :return:
    """
    k = random.randint(p, r)
    A[k], A[r] = A[r], A[k]
    i, j = p, p - 1
    x = A[r]
    while i < r:
        if A[i] <= x:
            j += 1
            if i != j:
                A[i], A[j] = A[j], A[i]
        i += 1
    A[j + 1], A[r] = A[r], A[j + 1]
    return j + 1


def randomSelect(A, p, r, i):
    """
    返回A[p...r]中第i个枢纽点
    :param A:
    :param p:
    :param r:
    :param i:
    :return:
    """
    if p == r:
        return A[p]
    q = randomPartition(A, p, r)
    t = q - p + 1
    if t == i:
        return A[q]
    elif t > i:
        return randomSelect(A, p, q - 1, i)
    else:
        return randomSelect(A, q + 1, r, i-t)


if __name__ == "__main__":
    nums = [9, 4, 8, 3, 2, 5, 7]
    print(getMinMax(nums))
    for i in range(10):
        print(randomSelect(nums, 0, len(nums) - 1, 1))
