#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 上午10:15
# @Author  : pengyuan.li
# @Site    : 
# @File    : 026_remove_duplicates.py
# @Software: PyCharm


def remove_duplicates(nums):
    """
    note:
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    else:
        out = 0
        for i in range(1, len_nums):
            if nums[out] != nums[i]:
                out = out + 1
                nums[out] = nums[i]
    return out + 1


def remove_duplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    i = 0
    j = 0
    while i < len_nums:
        if nums[i] != nums[j]:
            j = j + 1
            nums[j] = nums[i]
        i = i + 1

    return j + 1


if __name__ == "__main__":
    """
    删除重复数字，使用双指针法
    """
    nums = [1]
    len_nums = remove_duplicates(nums)
    for i in range(len_nums):
        print(nums[i])
    nums = [1, 1, 2]
    len_nums = remove_duplicates(nums)
    for i in range(len_nums):
        print(nums[i])
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    len_nums = remove_duplicates2(nums)
    for i in range(len_nums):
        print(nums[i])
