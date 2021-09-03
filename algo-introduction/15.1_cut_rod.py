#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def cutRod(p, n):
    """
    动态规划寻找最优分割，r[n]=max(p[i]+r[n-i]),i=1,2,...n
    :param p: 每段切割价格
    :param n:
    :return:
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    c = 1  # 每次截断的成本
    for i in range(1, n + 1):
        r[i] = p[i]
        s[i] = i
        for j in range(1, i):
            if r[i] < p[j] + r[i - j] - c:
                r[i] = p[j] + r[i - j] - c
                s[i] = j
    return r[n], s


def memoCutRod(p, n):
    r = [float("-inf")] * (n + 1)
    s = [0] * (n + 1)

    def subMemoCurRod(p, i, r, s):
        if r[i] >= 0:
            return r[i]
        if i == 0:
            q = 0
        else:
            q = float('-inf')
            for j in range(1, i + 1):
                # q = max(q, p[j] + subMemoCurRod(p, i - j, r))
                if q < p[j] + subMemoCurRod(p, i - j, r, s):
                    q = p[j] + subMemoCurRod(p, i - j, r, s)
                    s[i] = j
        r[i] = q
        return q

    return subMemoCurRod(p, n, r, s), s


def recursiveCutRod(p, n):
    """
    note:迭代求解
    :param p:
    :param n:
    :return: 活动的下标
    """
    if n == 0:
        return p[n]
    else:
        res = float('-inf')
        for i in range(1, n + 1):
            res = max(res, p[i] + recursiveCutRod(p, n - i))
    return res


if __name__ == "__main__":
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(p) - 1
    print(cutRod(p, n))
    print(recursiveCutRod(p, n))
    print(memoCutRod(p, n))
