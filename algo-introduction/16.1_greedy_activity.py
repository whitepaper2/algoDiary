#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def greedyFirstFinish(startTimes, finishTimes):
    """
    note:优先选择最早结束时间的活动，第一个是哨兵
    :param startTimes: 开始时间
    :param finishTimes: 结束时间（默认递增）
    :return: 活动的下标
    """
    lastF = finishTimes[0]
    out = []
    for i in range(1, len(finishTimes)):
        if startTimes[i] >= lastF:
            out.append(i)
            lastF = finishTimes[i]
    return out


def recursiveFirstFinish(startTimes, finishTimes):
    """
    note:迭代求解
    :param startTimes: 开始时间
    :param finishTimes: 结束时间（默认递增）
    :return: 活动的下标
    """
    n = len(startTimes)

    def subRecursive(startTimes, finishTimes, curi, n):
        m = curi + 1
        while m < n and startTimes[m] < finishTimes[curi]:
            m += 1
        if m < n:
            return [m] + subRecursive(startTimes, finishTimes, m, n)
        else:
            return []

    return subRecursive(startTimes, finishTimes, 0, n)


if __name__ == "__main__":
    startTimes = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finishTimes = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(greedyFirstFinish(startTimes, finishTimes))
    print(recursiveFirstFinish(startTimes, finishTimes))
