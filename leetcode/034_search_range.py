#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 下午4:20
# @Author  : pengyuan.li
# @Site    : 
# @File    : 034_search_range.py
# @Software: PyCharm
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    t = searchFirst(nums, target, 0, len(nums) - 1)
    left = t
    right = t
    if t == -1:
        return [-1, -1]
    else:
        while left > 0 and nums[left - 1] == target:
            left = left - 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right = right + 1
    return [left, right]


def searchFirst(nums: List[int], target: int, left: int, right: int) -> int:
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            return mid
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    # print(searchRange(nums, target))

    print(searchFirst(nums, target, 0, len(nums) - 1))
