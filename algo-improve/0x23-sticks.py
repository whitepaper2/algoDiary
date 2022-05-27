#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/05/23 19:27:04
@Author  : pengyuan.li
@File    : 0x23-sticks.py
@Software: VSCode
'''

# here put the import lib

from typing import List


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
            if not isVisited[
                    i] and cab + sticks[i] <= curlen and fail != sticks[i]:
                isVisited[i] = 1
                if dfs(idx, cab + sticks[i], i + 1, cnt, curlen):
                    return True
                fail = sticks[i]
                isVisited[i] = 0
                if cab == 0 and cab + sticks[i] == curlen:
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


if __name__ == "__main__":
    sticks = [5, 2, 1, 5, 2, 1, 5, 2, 1]
    print(minStickLength(sticks))
    sticks = [1, 2, 3, 4]
    print(minStickLength(sticks))