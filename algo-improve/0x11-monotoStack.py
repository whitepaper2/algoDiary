#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 上午11:18
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20210922_monotoStack.py
# @Software: PyCharm

"""
单调栈和单调队列
数列为：6 4 10 10 8 6 4 2 12 14
N=10,K=3;
求从左至右输出每个长度为𝑘的数列段内的最小数和最大数
=> 输出 6,6,10,10,10,10,8,6,12,14
"""
from collections import deque


def bruteMethod(nums, K):
    """
    算法复杂度：O(N*K)
    :param nums:
    :param K: 间隔单位
    :return:
    """
    n = len(nums)
    fmin = list()
    fmax = list()
    for i in range(n):
        startK = max(i - K, -1)
        maxM = nums[i]
        minM = nums[i]
        for j in range(startK + 1, i):
            maxM = max(nums[j], maxM)
            minM = min(nums[j], minM)
        fmax.append(maxM)
        fmin.append(minM)
    return fmax, fmin


def montonoDeque(nums, K):
    n = len(nums)
    maxQueue = deque(maxlen=K)
    fmax = list()
    minQueue = deque(maxlen=K)
    fmin = list()
    for i in range(n):
        while maxQueue and maxQueue[-1] <= nums[i]:
            maxQueue.pop()
        maxQueue.append(nums[i])
        fmax.append(maxQueue[0])

        if len(minQueue) == K:
            minQueue.popleft()
        while minQueue and minQueue[-1] > nums[i]:
            minQueue.pop()
        minQueue.append(nums[i])
        fmin.append(minQueue[0])
    return fmax, fmin


"""
找到原序列长度k的子序列中字典序最小的一个
"""


def minSubStr(s: str, k: int):
    """
    单调递增栈
    :param s:
    :param k: 1<=k<len(s)
    :return:
    """
    stack = deque()
    n = len(s)
    delCnts = n - k
    for i in range(n):
        while stack and delCnts > 0 and stack[-1] > s[i]:
            stack.pop()
            delCnts -= 1
        if delCnts == 0:
            res = []
            while stack:
                res.append(stack.pop())
            res.reverse()
            res += s[i:]
            return "".join(res)
        stack.append(s[i])
    res = []
    while stack:
        stack.append(stack.pop())
    res.reverse()
    return res


if __name__ == "__main__":
    nums = [6, 4, 10, 10, 8, 6, 4, 2, 12, 14]
    K = 3
    print(bruteMethod(nums, K))
    print(montonoDeque(nums, K))

    s = "helloworld"
    k = 5
    print(minSubStr(s, k))
