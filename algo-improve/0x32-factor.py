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
    for i in range(N + 1):
        factor[i] = []
    for i in range(1, N + 1):
        j = 1
        while i * j <= N:
            factor[i * j].append(i)
            j += 1
    return factor[1:]


def inversePrime(N):
    """
    对于任何正整数 x，其约数的个数记作 g(x)，例如 g(1)=1、g(6)=4。
    如果某个正整数 x 满足：对于任意的小于 x 的正整数 i，都有 g(x)>g(i)，则称 x 为反素数。
    :param N:
    :return:
    """
    # 素数的指数单调递减
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    maxN = 0
    maxP = 0

    def dfs(cur, last, pcnts, res):
        """
        :param cur: 当前因子的下标
        :param last: 上一因子的指数
        :param pcnts: 因子个数
        :param res:当前积
        :return:
        """
        nonlocal maxN
        nonlocal maxP
        if pcnts > maxP or pcnts == maxP and maxN > res:
            maxP = pcnts
            maxN = res
        if cur >= len(primes):
            return
        for i in range(1, last + 1):
            if res * primes[cur] > N:
                break
            res *= primes[cur]
            dfs(cur + 1, i, pcnts * (i + 1), res)

    dfs(0, 30, 1, 1)
    return maxN


if __name__ == "__main__":
    N = 100
    print(factors(N))
    print(rangeFactors(10))
    print(inversePrime(1000))
