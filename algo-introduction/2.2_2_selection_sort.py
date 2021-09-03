#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm


def selection_sort(nums):
    """
    note: 算法导论-2.2-2练习题：选择排序，非升序
    :param nums: List[Int]
    :return: List[Int]
    """
    for i in range(0, len(nums) - 1):
        minm = nums[i]
        k = i
        for j in range(i + 1, len(nums)):
            if nums[j] < minm:
                minm = nums[j]
                k = j
        if k != i:
            nums[i], nums[k] = nums[k], nums[i]
    return nums


if __name__ == "__main__":
    nums = [31, 41, 59, 26, 41, 58]
    print(selection_sort(nums))
