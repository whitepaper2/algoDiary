#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午4:20
# @Author  : pengyuan.li
# @Site    : 
# @File    : 004_radix_sort.py
# @Software: PyCharm
from typing import List


def radix_sort(nums):
    """
    note: 基数排序
    :param nums: 待排序数组
    :return:
    """
    # 不足位数的，前排加0
    nums_fill0 = []
    x_len = [len(str(nums[i])) for i in range(len(nums))]
    max_x_len = max(x_len)
    for i in range(len(nums)):
        if x_len[i] != max_x_len:
            ele = '0'*(max_x_len-x_len[i]) + str(nums[i])
        else:
            ele = str(nums[i])
        nums_fill0.append(ele)
    for i in range(max_x_len - 1, -1, -1):
        # 分配十个list
        digit_list: List[List[str]] = [[], [], [], [], [], [], [], [], [], []]
        for j in range(len(nums_fill0)):
            ele = nums_fill0[j]
            for k in range(10):
                if int(ele[i]) == k:
                    digit_list[k].append(ele)
        nums_fill0 = [x for y in digit_list for x in y]
        print(nums_fill0)
        digit_list.clear()
    return [int(x) for x in nums_fill0]


if __name__ == "__main__":
    nums = [3097, 3673, 2985, 1358, 6138, 9135, 4782, 1367, 3684, 139]
    nums = radix_sort(nums)
    print(nums)
    # 按照年、月、日，日期排序
    nums = [20201001, 20200801, 20190909, 20210908, 20201101, 20200802, 20201009, 20201103, 20201208, 20210101]
    nums = radix_sort(nums)
    print(nums)
    print(bin(3097))
    print(bin(16))
