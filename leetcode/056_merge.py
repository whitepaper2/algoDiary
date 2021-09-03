#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 下午7:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 056_merge.py
# @Software: PyCharm

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []
    intervals.sort()
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= stack[-1][1]:
            tmp = stack.pop()
            end = intervals[i][1] if intervals[i][1] > tmp[1] else tmp[1]
            stack.append([tmp[0], end])
        else:
            stack.append(intervals[i])
    return stack


# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
