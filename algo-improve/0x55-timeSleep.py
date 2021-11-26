#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 下午4:41
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x55-timeSleep.py
# @Software: PyCharm


def timeSleep(energy, times):
    """
    休息times，获得最大化能量值
    破环为链，双倍
    :param energy:
    :param times:
    :return:
    """
    n = len(energy)
    energy.insert(0, 0)
    dp0 = [[float('-inf') for _ in range(times + 1)] for _ in range(n + 1)]
    dp1 = [[float('-inf') for _ in range(times + 1)] for _ in range(n + 1)]
    dp0[1][0] = 0
    dp1[1][1] = 0
    for i in range(2, n + 1):
        for j in range(0, min(times, i) + 1):
            dp0[i][j] = max(dp0[i - 1][j], dp1[i - 1][j])
            dp1[i][j] = max(dp0[i - 1][j - 1], dp1[i - 1][j - 1] + energy[i])
    res = max(dp0[n][times], dp1[n][times])

    dp0 = [[float('-inf') for _ in range(times + 1)] for _ in range(n + 1)]
    dp1 = [[float('-inf') for _ in range(times + 1)] for _ in range(n + 1)]
    dp1[1][1] = energy[1]
    for i in range(2, n + 1):
        for j in range(0, min(times, i) + 1):
            dp0[i][j] = max(dp0[i - 1][j], dp1[i - 1][j])
            dp1[i][j] = max(dp0[i - 1][j - 1], dp1[i - 1][j - 1] + energy[i])
    res = max(res, dp1[n][times])
    return res


def transport(nums):
    """
    环路运输，nums[i]+nums[j]+abs(i-j)
    :param nums:
    :return:
    """
    n = len(nums)
    A = [0] + nums * 2
    sumDict = {}
    for i, e in enumerate(A):
        sumDict[(i, e)] = e - i
    print(A)
    res = 0
    for i in range(1, 2 * n + 1):
        for j in range(max(i - n // 2, 0), i):
            res = max(res, A[i] + i + sumDict[(j, A[j])])
    return res


def transport2(nums):
    """
    环路运输，nums[i]+nums[j]+abs(i-j)
    :param nums:
    :return:
    """
    n = len(nums)
    A = [0] + nums * 2
    N = n // 2
    res = 0
    left, right = 1, 1
    queue = [0] * (2 * n + 1)  # 递减队列, 值=queue[i]-i
    for i in range(1, n + N):
        while left <= right and i - queue[left] > N:
            left += 1
        res = max(res, A[i] + i + A[queue[left]] - queue[left])
        while left <= right and A[queue[right]] - queue[right] < A[i] - i:
            right -= 1
        right += 1
        queue[right] = i
    return res


if __name__ == "__main__":
    energy = [2, 0, 3, 1, 4]
    times = 3
    print(timeSleep(energy, times))

    nums = [1, 8, 6, 2, 5]
    print(transport(nums))

    nums = [1, 8, 6, 2, 5]
    print(transport2(nums))
