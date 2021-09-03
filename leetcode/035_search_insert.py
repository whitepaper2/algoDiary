#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 下午7:39
# @Author  : pengyuan.li
# @Site    : 
# @File    : 035_search_insert.py
# @Software: PyCharm
from common import timeit


@timeit
def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    len_nums = len(nums)
    out = 0
    while out < len_nums:
        if nums[out] >= target:
            break
        out = out + 1
    return out


@timeit
def search_insert2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    if nums[len_nums - 1] < target:
        return len_nums
    start = 0
    end = len_nums
    while start < end:
        middle = int((start + end) / 2)
        if nums[middle] > target:
            end = middle
            temp = middle - 1
            if temp >= 0:
                if nums[temp] < target:
                    return temp + 1
            else:
                return 0
        elif nums[middle] < target:
            start = middle
            temp = middle + 1
            if temp < len_nums:
                if nums[temp] > target:
                    return temp
            else:
                return len_nums
            pass
        else:
            return middle


if __name__ == "__main__":
    """
    method2 is so faster than method1
    """
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert2(nums, target))
    nums = [1, 3, 5, 6]
    target = 2
    print(search_insert2(nums, target))
    nums = [1, 3, 5, 6]
    target = 7
    print(search_insert2(nums, target))
    nums = [1, 3, 5, 6]
    target = 0
    print(search_insert2(nums, target))
