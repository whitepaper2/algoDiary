#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 上午11:21
# @Author  : pengyuan.li
# @Site    : 
# @File    : double-week64.py
# @Software: PyCharm

"""
2054. 两个最好的不重叠活动
给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，
结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。

请你返回价值之和的 最大值 。

注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，
如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。
"""
from typing import List


class Event(object):
    def __init__(self, ts, op, val):
        self.ts = ts
        self.op = op
        self.val = val

    def __lt__(self, other: 'Event'):
        return (self.ts, self.op) < (other.ts, other.op)


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        已经结束的活动可作为bestFirst，开始的作为Second
        :param events:
        :return:
        """
        eventList = []
        for startT, endT, val in events:
            eventList.append(Event(startT, 0, val))
            eventList.append(Event(endT, 1, val))
        eventList.sort()
        res = 0
        bestFirst = 0
        for t in eventList:
            if t.op == 1:
                bestFirst = max(t.val, bestFirst)
            else:
                res = max(res, bestFirst + t.val)
        return res


if __name__ == "__main__":
    events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    sins = Solution()
    print(sins.maxTwoEvents(events))
