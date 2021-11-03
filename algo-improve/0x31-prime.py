#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 下午3:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x31-prime.py
# @Software: PyCharm
import math


def isPrime(N):
    """
    判断是否为素数, N>=2 ,只能被1和N整除
    N的因子不超过 sqrt(N)
    :param N:
    :return:
    """
    assert N > 2
    for p in range(2, int(math.sqrt(N)) + 1):
        if N % p == 0:
            return False
    return True


def rangePrimes(N):
    """
    [2,N]区间的素数
    method1.遍历区间内每个值，调用isPrime(n)
    method2.艾德拉晒选
    :param N:
    :return:
    """
    nonPrimes = [0] * (N + 1)
    for p in range(2, N + 1):
        if nonPrimes[p] == 0:
            i = 2
            while i * p < N + 1:
                nonPrimes[i * p] = 1
                i += 1
        p += 1
    return [i for i, x in enumerate(nonPrimes) if i > 1 and x == 0]


def primeDistance(L, R):
    """
    [L,R]区间内两相邻素数的最大距离，并输出两素数
    1<L<R<2^31 and R-L<10^6
    :param L:
    :param R:
    :return:
    """
    primes = rangePrimes(int(math.sqrt(R)) + 1)
    nonPrimes = {x: 0 for x in range(L, R + 1)}
    for p in primes:
        i = L // p
        while i * p <= R:
            if i * p >= L:
                nonPrimes[i * p] = 1
            i += 1
    primeList = [k for k, v in nonPrimes.items() if v == 0]
    # 得到最后的最大值
    primeList.reverse()
    res = 0
    left = -1
    right = -1
    for i in range(len(primeList) - 1):
        if primeList[i] - primeList[i + 1] > res:
            res = primeList[i] - primeList[i + 1]
            left = primeList[i + 1]
            right = primeList[i]
    return res, left, right


def primeFactor(N):
    """
    质因子分解：97532468=2^2*11*17*101*1291
    质因子递增顺序排列
    :param N: > 0
    :return:
    """
    primes = []
    inds = []
    p = 2
    while p <= int(math.sqrt(N)) + 1:
        if N % p == 0:
            if primes and primes[-1] == p:
                inds[-1] += 1
            else:
                primes.append(p)
                inds.append(1)
            N = N // p
        else:
            p += 1
    if N > 1:
        primes.append(N)
        inds.append(1)
    resList = list()
    for p, i in zip(primes, inds):
        if i > 1:
            resList.append(str(p) + '^' + str(i))
        else:
            resList.append(str(p))
    return "*".join(resList)


def primeFactor2(N):
    """
    质因子分解：97532468=2^2*11*17*101*1291
    质因子递增顺序排列
    :param N: > 0
    :return:
    """
    primes = []
    inds = []
    for p in range(2, int(math.sqrt(N)) + 1):
        if N % p == 0:
            primes.append(p)
            inds.append(0)
            while N % p == 0:
                N = N // p
                inds[-1] += 1
        p += 1
    if N > 1:
        primes.append(N)
        inds.append(1)
    resList = [str(p) + '^' + str(i) if i > 1 else str(p) for p, i in zip(primes, inds)]
    return "*".join(resList)


if __name__ == "__main__":
    N = 97532468
    print(primeFactor(N))
    print(primeFactor2(N))
    print(isPrime(N))
    print(rangePrimes(10000))
    print(primeDistance(10, 10000))
