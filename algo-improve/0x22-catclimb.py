#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/05/13 11:39:10
@Author  : pengyuan.li
@File    : 0x22-catclimb.py
@Software: VSCode
'''

# here put the import lib
from typing import List
from bitarray import bitarray


def catclimb(weight: List[int], maxWeight: int) -> int:
    """
    每辆车的承载量不能超过maxWeight，求使用最少的车运送小猫下山。
    weight:小猫的重量
    maxWeight:每辆车的最大承载量
    """
    weight.sort(reverse=True)
    n = len(weight)
    res = n
    # 车辆实际装载重量
    cab = [0] * (n + 1)

    def dfs(now, cnt):
        """
        now:当前处理第几个小猫
        cnt:当前已安排的车辆个数
        """
        nonlocal res
        if cnt > res:
            return
        if now == n:
            res = min(res, cnt)
            return
        for i in range(cnt):
            if weight[i] + weight[now] <= maxWeight:
                cab[i] += weight[now]
                dfs(now + 1, cnt)
                cab[i] -= weight[now]
        cab[cnt + 1] += weight[now]
        dfs(now + 1, cnt + 1)
        cab[cnt + 1] -= weight[now]

    dfs(0, 0)
    return res


def str2Mat(strs):
    out = []
    for i in range(0, len(strs), 9):
        out.append(strs[i:i + 9])
    return out


def sudoku(strs):
    out = []
    for i in range(0, len(strs), 9):
        out.append(strs[i:i + 9])
    N = 9
    M = 1 << N
    rows = [bitarray('0' * N) for _ in range(N)]
    cols = [bitarray('0' * N) for _ in range(N)]
    cells = [[bitarray('0' * N)] * 3 for _ in range(3)]
    onecnts = [0] * M
    mydict = [0] * M

    def lowbit(x):
        return x & (-x)

    for i in range(M):
        mydict[1 << i] = i

    for i in range(M):
        j = i
        while j > 0:
            onecnts[i] += 1
            j -= lowbit(j)
    
    
    print(cells)
    return out


if __name__ == "__main__":
    weight = [1, 2, 1994, 12, 29]
    maxWeight = 1996
    print(catclimb(weight, maxWeight))

    weight = [1000, 1003, 1994, 1200, 1290]
    maxWeight = 1996
    print(catclimb(weight, maxWeight))

    strs = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    print(sudoku(strs))
    "417369825632158947958724316825437169791586432346912758289643571573291684164875293"