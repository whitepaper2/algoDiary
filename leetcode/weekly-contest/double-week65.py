#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 上午10:11
# @Author  : pengyuan.li
# @Site    : 
# @File    : double-week65.py
# @Software: PyCharm

"""
2071. 你可以安排的最多任务数目
给你 n 个任务和 m 个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 0 开始的整数数组 tasks 中，第 i 个任务需要 tasks[i] 的力量才能完成。
每个工人的力量值保存在下标从 0 开始的整数数组 workers 中，第 j 个工人的力量值为 workers[j] 。
每个工人只能完成 一个 任务，且力量值需要 大于等于 该任务的力量要求值（即 workers[j] >= tasks[i] ）。

除此以外，你还有 pills 个神奇药丸，可以给 一个工人的力量值 增加 strength 。你可以决定给哪些工人使用药丸，但每个工人 最多 只能使用 一片 药丸。

给你下标从 0 开始的整数数组tasks 和 workers 以及两个整数 pills 和 strength ，请你返回 最多 有多少个任务可以被完成。
"""

from typing import List
from sortedcontainers import SortedList


def maxTaskAssign(tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
    """
    二分+贪心
    :param tasks:
    :param workers:
    :param pills:
    :param strength:
    :return:
    """
    n, m = len(tasks), len(workers)
    tasks.sort()
    workers.sort()

    def check(mid):
        p = pills
        ws = SortedList(workers[m - mid:])
        for i in range(mid - 1, -1, -1):
            if ws[-1] >= tasks[i]:
                ws.pop()
            else:
                if p == 0:
                    return False
                rep = ws.bisect_left(tasks[i] - strength)
                if rep == len(ws):
                    return False
                p -= 1
                ws.pop(rep)

        return True

    left, right, res = 0, min(n, m), 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


if __name__ == "__main__":
    tasks = [3, 2, 1]
    workers = [0, 3, 3]
    pills = 1
    strength = 1
    print(maxTaskAssign(tasks, workers, pills, strength))
