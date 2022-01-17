#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/17 09:57:20
@Author  : pengyuan.li
@File    : week276.py
@Software: VSCode
'''

# here put the import lib
from typing import List
"""
5983. 同时运行 N 台电脑的最长时间 

你有 n 台电脑。给你整数 n 和一个下标从 0 开始的整数数组 batteries ，其中第 i 个电池可以让一台电脑 运行 batteries[i] 分钟。
你想使用这些电池让 全部 n 台电脑 同时 运行。

一开始，你可以给每台电脑连接至多一个电池 。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，
你可以进行这个操作 任意次 。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。

注意，你不能给电池充电。
请你返回你可以让 n 台电脑同时运行的 最长 分钟数。
"""


class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        resuidal = sum(batteries[n:])

        def isValid(k):
            """
            只需要积累当前电量不足时需要补充的电量，多余的不计（因为被占用状态）
            need <= resuidal <= resuidal+newadd
            """
            need = 0
            for i in range(n):
                if batteries[i] < k:
                    need += k - batteries[i]
            return need <= resuidal

        left, right = 0, 10 ** 16
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


if __name__ == "__main__":
    # n = 2
    # batteries = [1, 1, 1, 1]
    # ss = Solution()
    # print(ss.maxRunTime(n, batteries))

    # n = 2
    # batteries = [3, 3, 3]
    # ss = Solution()
    # print(ss.maxRunTime(n, batteries))

    n = 1
    batteries = [53,96]
    ss = Solution()
    print(ss.maxRunTime(n, batteries))
