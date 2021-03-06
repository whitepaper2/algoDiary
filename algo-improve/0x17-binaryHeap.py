#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 上午10:48
# @Author  : pengyuan.li
# @Site    :
# @File    : 0x17-binaryHeap.py
# @Software: PyCharm
"""
poj145：超市里有 N 件商品，每件商品都有利润 pi 和过期时间 di，每天只能卖一件商品，过期商品不能再卖。
求合理安排每天卖的商品的情况下，可以得到的最大收益是多少。
"""

import heapq


def maxProfit(foods):
    """
    按过期时间排序，遍历每一个商品，加入最小堆，1.若过期时间=堆大小，再比较堆头和当前商品价值大小；2.过期时间>堆大小，直接入堆
    全部遍历完成后，计算堆
    :param foods: [[pi,di]]
    :return:
    """
    foods.sort(key=lambda x: x[1])
    minHeap = []
    heapq.heapify(minHeap)
    for p, d in foods:
        if d > len(minHeap):
            heapq.heappush(minHeap, (p, d))
        else:
            minp, mind = minHeap[0]
            if minp < p:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (p, d))
    return sum([p for p, d in minHeap])


def topNsum(A, B, N):
    """
    简化问题，len(nums)=2,若长度>2,则两两计算生成1个新序列再与其他序列构成。
    1、初始化(0,0,False) 是否加入j
    2、循环，(i,j,last),加入(i,j+1,True),如果last=False,加入(i+1,j,False)
    """
    A.sort()
    B.sort()
    minHeap = [(A[0] + B[0], 0, 0, False)]
    m, n = len(A), len(B)
    heapq.heapify(minHeap)
    tot = 0
    res = []
    while tot < N and minHeap:
        v, i, j, flag = heapq.heappop(minHeap)
        tot += 1
        res.append(v)
        if j + 1 < n:
            heapq.heappush(minHeap, (A[i] + B[j + 1], i, j + 1, True))
        if i + 1 < m and not flag:
            heapq.heappush(minHeap, (A[i + 1] + B[j], i + 1, j, False))
    return res


if __name__ == "__main__":
    foods = [[20, 1], [2, 1], [10, 3], [100, 2], [8, 2], [5, 20], [50, 10]]
    print(maxProfit(foods))

    foods = [[50, 2], [10, 1], [20, 2], [30, 1]]
    print(maxProfit(foods))

    # nums = [[1, 2, 3], [2, 2, 3], [8,2,4]]
    A = [1, 2, 3]
    B = [2, 2, 3]
    N = 3
    print(topNsum(A, B, N))
    nums = [1,3,4,6,12]