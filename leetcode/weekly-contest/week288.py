#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/24 13:25:30
@Author  : pengyuan.li
@File    : week288.py
@Software: VSCode
'''

# here put the import lib
from typing import List
"""
2234. 花园的最大总美丽值
Alice 是 n 个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。
给你一个下标从 0 开始大小为 n 的整数数组 flowers ，其中 flowers[i] 是第 i 个花园里已经种的花的数目。已经种了的花 不能 移走。
同时给你 newFlowers ，表示 Alice 额外可以种花的 最大数目 。同时给你的还有整数 target ，full 和 partial 。
如果一个花园有 至少 target 朵花，那么这个花园称为 完善的 ，花园的 总美丽值 为以下分数之 和 ：

完善 花园数目乘以 full.
剩余 不完善 花园里，花的 最少数目 乘以 partial 。如果没有不完善花园，那么这一部分的值为 0 。
请你返回 Alice 种最多 newFlowers 朵花以后，能得到的 最大 总美丽值。
"""


class Solution:

    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int,
                      full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        A = [0] * (n + 1)
        for i in range(n):
            A[i + 1] = flowers[i]
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + A[i]
        start = 0
        while start < n:
            if A[n - start] < target:
                break
            start += 1
        sm = 0
        res = 0
        i = start
        while i <= n and sm <= newFlowers:
            head, tail = 0, n - i
            while head < tail:
                mid = (head + tail + 1) >> 1
                t = mid * A[mid] - f[mid]
                if sm + t <= newFlowers:
                    head = mid
                else:
                    tail = mid - 1
            x = newFlowers - sm - (head * A[head] - f[head])
            y = min(A[head] + x // head if head > 0 else 0, target - 1)
            res = max(res, i * full + y * partial)
            sm += target - A[n - i]
            i += 1
        return res


if __name__ == "__main__":
    flowers = [1, 3, 1, 1]
    newFlowers = 7
    target = 6
    full = 12
    partial = 1
    ss = Solution()
    print(ss.maximumBeauty(flowers, newFlowers, target, full, partial))
