#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 下午10:42
# @Author  : pengyuan.li
# @Site    : 
# @File    : 137_single_number.py
# @Software: PyCharm


def single_number(nums):
    """
    note: 3*(a+b)-(a+b+a+a) = 2*b
    :type nums: List[int]
    :rtype: int
    """
    return int((3 * sum(list(set(nums))) - sum(nums)) / 2)


if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    print(single_number(nums))
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(single_number(nums))
