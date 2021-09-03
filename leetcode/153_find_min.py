#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 下午6:59
# @Author  : pengyuan.li
# @Site    : 
# @File    : 153_find_min.py
# @Software: PyCharm
# 二分查找最小值
from typing import List


def find_min(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[right]


def find_min2(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] == nums[right]:
            return min(find_min2(nums[left:mid]), find_min2(nums[mid+1:right+1]))
        else:
            right = mid
    return nums[right]


def find_max(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid
        else:
            right = mid - 1
    return nums[left]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))
    print(find_max(nums))
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(find_min(nums))
    print(find_max(nums))

    nums = [2, 2, 2, 2, 0, 1]
    print(find_min2(nums))
    nums = [3, 3, 1, 3]
    print(find_min2(nums))
