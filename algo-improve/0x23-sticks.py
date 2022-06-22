#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/05/23 19:27:04
@Author  : pengyuan.li
@File    : 0x23-sticks.py
@Software: VSCode
'''

# here put the import lib

import cProfile
from typing import List
import math


def minStickLength(sticks: List[int]) -> int:
    n = len(sticks)
    total = sum(sticks)
    maxLen = max(sticks)
    sticks.sort(reverse=True)
    res = 0
    isVisited = [0] * n

    def dfs(idx, cab, last, cnt, curlen):
        """
        @idx:拼接第 idx 根木棒，
        @cab:当前已拼接的木棒长度
        @last:最近使用过的木棒
        @cnt\curlen:可选的原始木棒长度和个数
        @return: T/F
        """

        if idx >= cnt:
            return True
        if cab == curlen:
            return dfs(idx + 1, 0, 0, cnt, curlen)
        fail = 0
        for i in range(last, n):
            # 不再搜索上次相同的失败匹配
            if not isVisited[
                    i] and cab + sticks[i] <= curlen and fail != sticks[i]:
                isVisited[i] = 1
                if dfs(idx, cab + sticks[i], i + 1, cnt, curlen):
                    return True
                fail = sticks[i]
                isVisited[i] = 0
                if cab == 0 or cab + sticks[i] == curlen:
                    return False
        return False

    for curlen in range(maxLen, total + 1):
        if total % curlen:
            continue
        # 原始木棒长度curlen, 有curcnt个
        curcnt = total // curlen
        if dfs(1, 0, 0, curcnt, curlen):
            res = curlen
            break
    return res


def birthdayGift(N, M):
    """
    @N: 待制作 N*pi
    @M: 蛋糕层数
    @return: 蛋糕表面积
    """
    minv = [0] * (N + 2)
    mins = [0] * (N + 2)
    for i in range(1, M + 1):
        minv[i] = minv[i - 1] + i * i * i
        mins[i] = mins[i - 1] + 2 * i * i
    R = [0] * (N + 1)
    H = [0] * (N + 1)
    R[M + 1] = float('inf')
    R[M + 1] = float('inf')
    res = float('inf')
    

    def dfs(u, v, s):
        nonlocal res
        if v + minv[u] > N:
            return
        if s + mins[u] >= res:
            return
        if s + 2 * (N - v) / R[u + 1] >= res:
            return
        if not u:
            if v==N:
                res = s
            return
        for r in range(
                min(R[u + 1] - 1, int(math.sqrt((N - v - minv[u - 1]) / u))),
                -1, u - 1):
            for h in range(
                    min(H[u + 1] - 1, int((N - v - minv[u - 1]) / r / r)), -1,
                    u - 1):
                H[u] = h
                R[u] = r
                t = r * r if u == M else 0
                dfs(u - 1, v + r * r * h, s + 2 * r * h + t)

    dfs(M, 0, 0)
    if res == float('inf'):
        res = 0
    return res


if __name__ == "__main__":
    sticks = [5, 2, 1, 5, 2, 1, 5, 2, 1]
    print(minStickLength(sticks))
    # 性能分析函数 cProfile
    cProfile.run('minStickLength(sticks)')
    sticks = [1, 2, 3, 4]
    print(minStickLength(sticks))
    n, m = 100, 2
    print(birthdayGift(n, m))
