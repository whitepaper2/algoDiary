#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 下午6:48
# @Author  : pengyuan.li
# @Site    : 
# @File    : 080_remove_duplicates.py
# @Software: PyCharm

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    for i in range(len(nums) - 1, 1, -1):
        if nums[i] == nums[i - 2]:
            del nums[i]
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print(remove_duplicates(nums))
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(remove_duplicates(nums))
