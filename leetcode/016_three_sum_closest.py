#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午5:40
# @Author  : pengyuan.li
# @Site    : 
# @File    : 016_three_sum_closest.py
# @Software: PyCharm


def three_sum_closest(nums, target):
    """
    note: 固定一值，双指针遍历另两值。
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    closest = nums[0] + nums[1] + nums[2]
    diff = abs(closest - target)
    sorted_nums = sorted(nums)
    for i in range(len(nums) - 1):
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            cur_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            new_diff = abs(cur_sum - target)
            if new_diff < diff:
                diff = new_diff
                closest = cur_sum
            if cur_sum > target:
                right = right - 1
            else:
                left = left + 1

    return closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(three_sum_closest(nums, target))
