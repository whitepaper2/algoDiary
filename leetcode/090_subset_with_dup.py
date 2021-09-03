#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 下午9:07
# @Author  : pengyuan.li
# @Site    : 
# @File    : 090_subset_with_dup.py
# @Software: PyCharm


def subsets_with_dup(nums):
    """
    note:与无重复数值的差别，记录上次数组长度
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from copy import deepcopy
    out = [[]]
    sort_nums = sorted(nums)
    last = sort_nums[0]
    last_size = 0
    for i in range(len(sort_nums)):
        temp = deepcopy(out)
        temp_size = len(temp)
        if last == sort_nums[i]:
            temp2 = []
            for j in range(last_size, temp_size):
                temp[j].append(sort_nums[i])
                temp2.append(temp[j])
            temp = deepcopy(temp2)
            last_size = deepcopy(temp_size)
        else:
            last_size = temp_size
            last = sort_nums[i]
            for t in temp:
                t.append(sort_nums[i])

        out.extend(temp)
    return out


if __name__ == "__main__":
    nums = [2, 2, 2, 2,3,3]
    print(subsets_with_dup(nums))
