#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午5:21
# @Author  : pengyuan.li
# @Site    : 
# @File    : 189_rotate_array.py
# @Software: PyCharm


from typing import List


# 旋转数组，[1,2,3,4,5,6,7]->[5,6,7,1,2,3,4]
# 整体反转 + 前半部分反转 + 后半部分反转


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    k = k % nums_len
    reverse_array(nums, 0, nums_len - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, nums_len - 1)


def reverse_array(nums: List[int], left, right) -> None:
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left = left + 1
        right = right - 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)
