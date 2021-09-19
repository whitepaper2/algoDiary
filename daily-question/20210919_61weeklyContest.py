#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 上午9:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 20210919_61weeklyContest.py
# @Software: PyCharm

"""
判断并找出双倍数组的原值
"""
from collections import Counter


def findOriginArray(changed):
    """
    贪心+hash，考虑边界情况
    :param changed:
    :return:
    """
    cntDict = dict(Counter(changed))
    sortKeys = sorted([k for k, v in cntDict.items()])
    print(sortKeys)
    res = []
    for k in sortKeys:
        if k == 0:
            if cntDict[k] % 2 == 1:
                return []
            else:
                res += [0] * (cntDict[k] // 2)
        elif cntDict[k] > 0:
            if 2 * k not in cntDict:
                return []
            else:
                if cntDict[k] > cntDict[2 * k]:
                    return []
                else:
                    res += [k] * cntDict[k]
                    cntDict[2 * k] = cntDict[2 * k] - cntDict[k]
    return res


if __name__ == "__main__":
    changed = [1, 3, 4, 2, 6, 8]
    print(findOriginArray(changed))
    changed = [0, 0, 0, 0]
    print(findOriginArray(changed))
    changed = [2, 1, 2, 4, 2, 4]
    print(findOriginArray(changed))
    changed = [1, 2, 3, 2, 4, 6, 2, 4, 6, 4, 8, 12]
    print(findOriginArray(changed))
