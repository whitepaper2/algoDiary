#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 下午4:41
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x05-sort.py
# @Software: PyCharm

from typing import List
import collections


def delReplicate(A):
    """
    去重，离散化方法：先排序，相邻位置对比
    :param A:
    :return:
    """
    B = []
    A.sort()
    for i in range(len(A)):
        if i == 0 or A[i] != A[i - 1]:
            B.append(A[i])
    return B


def delReplicate2(A):
    """
    去重，离散化方法：先排序，相邻位置对比
    双指针，原地修改
    :param A:
    :return:
    """
    A.sort()
    n = len(A)
    j = 0
    i = 0
    while j < n:
        while i < n and A[j] == A[i]:
            i += 1
        if i == n:
            break
        j += 1
        A[j] = A[i]
    print(A)
    return A[:j+1]


def discrete(a: List[int], b: List[int], c: List[int]):
    """
    对于观影的科学家来说，如果能听懂电影的语音，他就会很开心；如果能看懂字幕，他就会比较开心；如果全都不懂，他就会不开心。
    现在科学家们决定大家看同一场电影。
    请你帮忙选择一部电影，可以让观影很开心的人最多。
    离散化，语言数量 <= 2*len(b)+len(a), len(b)==len(c)
    :param a: 科学家使用的语言
    :param b: 电影语音使用的语言
    :param c: 电影字幕使用的语言
    :return:
    """
    peopleDict = dict(collections.Counter(a))
    peoples = []
    k = 1
    for i, j in zip(b, c):
        peoples.append([peopleDict[i], peopleDict[j], k])
        k += 1
    peoples.sort(key=lambda x: (-x[0], -x[1]))
    return peoples[0][2]


if __name__ == "__main__":
    a = [2, 3, 2]
    b = [3, 2]
    c = [2, 3]
    print(discrete(a, b, c))

    print(delReplicate2(a))
