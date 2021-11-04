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
            res.extend([i, N // i])
    return res


if __name__ == "__main__":
    N = 100
    print(factors(N))
