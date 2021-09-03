#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 下午1:05
# @Author  : pengyuan.li
# @Site    : 
# @File    : 057_insert.py
# @Software: PyCharm
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    note: 顺序插入，遇到重叠的则合并
    :param intervals:
    :param newInterval:
    :return:
    """
    n = len(intervals)
    cur_i = 0
    out_stack = []
    while cur_i < n and intervals[cur_i][1] < newInterval[0]:
        out_stack.append(intervals[cur_i])
        cur_i = cur_i + 1
    while cur_i < n and intervals[cur_i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[cur_i][0], newInterval[0])
        newInterval[1] = max(intervals[cur_i][1], newInterval[1])
        cur_i = cur_i + 1
    out_stack.append(newInterval)
    while cur_i < n:
        out_stack.append(intervals[cur_i])
        cur_i = cur_i + 1
    return out_stack


# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))
    pass
