#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 下午5:47
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x32-factor.py
# @Software: PyCharm
import math


def factors(N):
    """
    整数N的因子分解
    :param N:
    :return:
    """
    res = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            res.append(i)
            if i != N // i:
                res.append(N // i)
    return res


def rangeFactors(N):
    """
    求[1,N]中每个数的正约数
    倍数法，不用遍历求每个值的约数
    :param N:
    :return:
    """
    factor = [0] * (N + 1)
    for i in range(N+1):
        factor[i] = []
    for i in range(1, N + 1):
        j = 1
        while i * j <= N:
            factor[i * j].append(i)
            j += 1
    return factor[1:]


if __name__ == "__main__":
    N = 100
    print(factors(N))
    print(rangeFactors(10))
