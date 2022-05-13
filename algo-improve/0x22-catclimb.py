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


if __name__ == "__main__":
    weight = [1, 2, 1994, 12, 29]
    maxWeight = 1996
    print(catclimb(weight, maxWeight))

    weight = [1000, 1003, 1994, 1200, 1290]
    maxWeight = 1996
    print(catclimb(weight, maxWeight))
