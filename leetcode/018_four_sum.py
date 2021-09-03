#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午7:02
# @Author  : pengyuan.li
# @Site    : 
# @File    : 018_four_sum.py
# @Software: PyCharm


def four_sum(nums, target):
    """
    note: 类似3sum，给数组排序，固定两个值，再逐个判别。
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    sorted_nums = sorted(nums)
    out = []
    for i in range(len(sorted_nums) - 3):
        for j in range(i + 1, len(sorted_nums) - 2):
            if j > i + 1 and sorted_nums[j] == sorted_nums[j - 1]:
                continue
            left = j + 1
            right = len(sorted_nums) - 1
            while left < right:
                cur_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[left] + sorted_nums[right]
                if target == cur_sum:
                    cur = [sorted_nums[i], sorted_nums[j], sorted_nums[left], sorted_nums[right]]
                    if cur not in out:
                        out.append(cur)
                    left += 1
                    right -= 1
                elif target > cur_sum:
                    left += 1
                else:
                    right -= 1
    return out


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(nums, target))
