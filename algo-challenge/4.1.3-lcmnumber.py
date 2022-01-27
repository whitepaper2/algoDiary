#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/26 17:42:56
@Author  : pengyuan.li
@File    : 4.1.3-lcmnumber.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def multiGcd(A):
    """
    求多个值的最大公约数
    """
    res = 1
    for i, v in enumerate(A):
        if i == 0:
            res = v
        else:
            res = gcd(res, v)
    return res


def multiGcd2(A):
    """
    求多个值的最大公约数,不断取出数组中最大值a和次大值b,若a%b==0，可删除a;否则
    """
    import heapq
    res = A[0]
    maxHeap = [-v for v in A]
    heapq.heapify(maxHeap)
    while len(maxHeap) > 1:
        p1 = -1 * heapq.heappop(maxHeap)
        p2 = -1 * heapq.heappop(maxHeap)
        if p1 == p2:
            res = p1
            break
        if p1 % p2 == 0:
            heapq.heappush(maxHeap, -1 * p2)
        else:
            heapq.heappush(maxHeap, -1 * (p1 % p2))
        heapq.heappush(maxHeap, -1 * p2)
    return res


def divisonCnts(A: List[int], N: int):
    """
    1-N中至少能整除A中一个元素的数有多少个
    容斥原理
    """
    m = len(A)
    res = 0
    for i in range(1, 1 << m):
        num = 0
        j = i
        while j != 0:
            num += j & 1
            j = j >> 1
        lcm = 1
        for j in range(m):
            if i >> j & 1:
                lcm = lcm * A[j] / gcd(lcm, A[j])
            if lcm > N:
                break
        if num % 2 == 0:
            res -= N / lcm
        else:
            res += N / lcm
    return res, round(res)


if __name__ == "__main__":
    nums = [3, 6, 9]
    print(gcd(1, 3))
    print(multiGcd(nums))
    nums = [6, 3]
    print(multiGcd2(nums))
    nums = [2, 3]
    n = 100
    print(divisonCnts(nums, n))
