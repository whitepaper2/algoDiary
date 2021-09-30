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


def sumOfBeauties(nums) -> int:
    res = 0
    n = len(nums)
    fmax = [0] * n
    fmax[0] = nums[0]

    for i in range(1, n - 1):
        if nums[i - 1] > fmax[i - 1]:
            fmax[i] = nums[i - 1]
        else:
            fmax[i] = fmax[i - 1]
    # print(fmax)
    fmin = [1e6] * n
    fmin[n - 1] = nums[n - 1]
    for i in range(n - 2, 0, -1):
        if nums[i + 1] < fmin[i + 1]:
            fmin[i] = nums[i + 1]
        else:
            fmin[i] = fmin[i + 1]
    # print(fmin)
    for i in range(1, n - 1):
        if fmax[i] < nums[i] < fmin[i]:
            res += 2
        elif nums[i - 1] < nums[i] < nums[i + 1]:
            res += 1

    return res


def longestSubsequenceRepeatedK(s: str, k: int) -> str:
    from collections import Counter
    sDict = dict(Counter(list(s)))
    keys = [k2 for k2, v in sDict.items() if v >= k]
    s2 = [ss for ss in s if ss in keys]
    n = len(s2)
    total = list()  # 存放所有回文子序列
    for i in range(1, 1 << n):  # 用位运算列出所有子序列
        temp = ''
        for j in range(n):
            if (1 << j) & i:
                temp += s2[j]
        total.append((i,temp))

    ret = list()
    for i in range(len(total)):
        kx, x = total[i]
        for j in range(i + 1, len(total)):
            ky, y = total[j]
            if kx & ky:
                continue
            if x ==y:
                ret.append(y)
    print(ret)
    #     if temp not in total:
    #         total[temp] = 1
    #     else:
    #         total[temp] += 1

    return ""


if __name__ == "__main__":
    changed = [1, 3, 4, 2, 6, 8]
    print(findOriginArray(changed))
    changed = [0, 0, 0, 0]
    print(findOriginArray(changed))
    changed = [2, 1, 2, 4, 2, 4]
    print(findOriginArray(changed))
    changed = [1, 2, 3, 2, 4, 6, 2, 4, 6, 4, 8, 12]
    print(findOriginArray(changed))
    nums = [1, 2, 3, 4, 5, 6, 6, 7]
    print(sumOfBeauties(nums))
    #todo:第259周赛的hard，遍历算法未完待续
    s = "letsleetcode"
    k = 2
    print(longestSubsequenceRepeatedK(s,k))

