#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 下午7:22
# @Author  : pengyuan.li
# @Site    : 
# @File    : 081_search.py
# @Software: PyCharm
from typing import List


def search(nums: List[int], target: int) -> bool:
    if nums is None:
        return False
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            if target > nums[right] >= nums[mid]:
                right = right - 1
            else:
                left = mid + 1
        else:
            if nums[mid] >= nums[left] > target:
                left = mid + 1
            else:
                right = mid - 1
    return False


def search2(nums: List[int], target: int) -> bool:
    if nums is None:
        return False
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        elif nums[right] < nums[mid]:
            if nums[mid] > target >= nums[left]:
                right = right - 1
            else:
                left = mid + 1
        elif nums[right] > nums[mid]:
            if nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            right = right - 1
    return False


if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(search2(nums, target))

    target = 3
    print(search2(nums, target))

    nums = [1]
    target = 1
    print(search2(nums, target))
    nums = [1, 1, 3, 1]
    target = 3
    print(search2(nums, target))
