#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 上午10:02
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.2.1-greedyExample.py
# @Software: PyCharm

from typing import List


def moneyExchange(coins: List[int], A: int) -> int:
    """
    本题采用贪心算法，可以找到最优解。但是该类问题不一定都能找到
    :param coins:[1,5,10,50,100,200]分别代表各面值硬币个数
    :param A:待兑换的钱
    :return:最少硬币数
    """
    res = 0
    money = [1, 5, 10, 50, 100, 500]
    n = len(coins)

    for i in range(n - 1, -1, -1):
        while A >= money[i] and coins[i] > 0:
            A -= money[i]
            res += 1
            coins[i] -= 1
    return res


def moneyExchange2(coins: List[int], A: int) -> int:
    """
    本题采用贪心算法，可以找到最优解。但是该类问题不一定都能找到
    :param coins:[1,5,10,50,100,200]分别代表各面值硬币个数
    :param A:待兑换的钱
    :return:最少硬币数
    """
    res = 0
    money = [1, 5, 10, 50, 100, 500]
    n = len(coins)

    for i in range(n - 1, -1, -1):
        cnt = min(A // money[i], coins[i])
        A -= cnt * money[i]
        res += cnt
    return res


def arrangeWorkTime(S: List[int], T: List[int]) -> int:
    """
    返回可以安排最大的工作量
    :param S: ith job start time
    :param T: ith job finish time
    :return:
    """
    jobs = [(s, t) for s, t in zip(S, T)]
    jobs.sort(key=lambda x: x[1])
    res = 0
    n = len(jobs)
    i = 0
    prevFinish = -1
    while i < n:
        if prevFinish < jobs[i][0]:
            res += 1
            prevFinish = jobs[i][1]
        i += 1
    return res


def regenerateStr(S: str) -> str:
    """
    每次从S的首部或尾部取一字符，生成字典序的字符串
    :param S:
    :return:
    """
    T = ''
    n = len(S)
    left, right = 0, n - 1
    while left <= right:
        isLeft = False
        i = 0
        while i + left <= right:
            if S[left + i] < S[right - i]:
                isLeft = True
                break
            if S[left + i] > S[right - i]:
                isLeft = False
                break
            i += 1
        if isLeft:
            T += S[left]
            left += 1
        else:
            T += S[right]
            right -= 1
    return T


def rangeFlag(A: List[int], R: int) -> int:
    """
    在坐标轴上标记点，该点覆盖半径R中的点，求最少标记点个数
    :param A:
    :param R:
    :return:
    """
    A.sort()
    res = 0
    i = 0
    n = len(A)
    while i < n:
        point = A[i]
        i += 1
        while i < n and point + R >= A[i]:
            i += 1
        flagPoint = A[i - 1]
        res += 1
        while i < n and flagPoint + R >= A[i]:
            i += 1
    return res


def repairFrench(A: List[int]) -> int:
    """
    工匠修理东西，类似于合并石头，每次可任意选择两个
    优先队列解答
    :param A:
    :return:
    """
    import heapq
    res = 0
    minHeap = A
    heapq.heapify(minHeap)
    while minHeap and len(minHeap) > 1:
        first = heapq.heappop(minHeap)
        second = heapq.heappop(minHeap)
        res += first + second
        heapq.heappush(minHeap, first + second)
    return res


if __name__ == "__main__":
    coins = [3, 2, 1, 3, 0, 2]
    A = 620
    print(moneyExchange(coins, A))

    coins = [3, 2, 1, 3, 0, 2]
    A = 620
    print(moneyExchange2(coins, A))

    startT = [1, 2, 4, 6, 8]
    endT = [3, 5, 7, 9, 10]
    print(arrangeWorkTime(startT, endT))

    s = "ACDBCB"
    print(regenerateStr(s))

    nums = [1, 7, 15, 20, 30, 50]
    r = 10
    print(rangeFlag(nums, r))

    nums = [8, 5, 8]
    print(repairFrench(nums))
