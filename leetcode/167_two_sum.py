#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 上午11:55
# @Author  : pengyuan.li
# @Site    : 
# @File    : 167_two_sum.py
# @Software: PyCharm

from typing import List


# 给定一个递增整数数组、一个目标值，求数组中两数之和=target
# 因为是排序数组，可以使用双指针法遍历求和。（不是二分法）


def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        left_val = numbers[left]
        right_val = numbers[right]
        if left_val + right_val == target:
            return [left + 1, right + 1]
        elif left_val + right_val < target:
            left = left + 1
        else:
            right = right - 1
    return [-1, -1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))
