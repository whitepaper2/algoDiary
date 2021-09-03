#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 下午4:16
# @Author  : pengyuan.li
# @Site    : 
# @File    : 075_sort_colors.py
# @Software: PyCharm]
from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    note: 记录0、1、2的个数，分别赋值
    """
    cnt_list = [0, 0, 0]
    for ele in nums:
        cnt_list[ele] = cnt_list[ele] + 1
    cur = 0
    for i in range(len(cnt_list)):
        for _ in range(cnt_list[i]):
            nums[cur] = i
            cur = cur + 1


def sortColors2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    note: 双指针法
    """
    left = 0
    right = len(nums) - 1
    cur = 0
    while cur <= right:
        if nums[cur] == 2:
            tmp = nums[right]
            nums[right] = nums[cur]
            nums[cur] = tmp
            right = right - 1
        elif nums[cur] == 0:
            tmp = nums[left]
            nums[left] = nums[cur]
            nums[cur] = tmp
            cur = cur + 1
            left = left + 1
        else:
            cur = cur + 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sortColors2(nums)
    print(nums)
