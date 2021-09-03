#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 下午10:25
# @Author  : pengyuan.li
# @Site    : 
# @File    : 001_two_sum.py
# @Software: PyCharm
# import timeit
from common import timeit


@timeit
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    len_nums = len(nums)
    nums_dict = {}
    for i in range(len_nums):
        nums_dict[nums[i]] = i
    for i in range(len_nums):
        if nums[i] <= target or nums[i] <= abs(target):
            v1 = target - nums[i]
            if nums_dict.get(v1) is not None and i != nums_dict.get(v1):
                return [i, nums_dict.get(v1)]


def twoSum2(nums, target):
    """
    遍历一次，字典记录不满足约束条件的值(值，索引)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}
    for i in range(len(nums)):
        cur_val = nums[i]
        others = target - cur_val
        if nums_dict.get(others) is not None and nums_dict.get(others) != i:
            return [i, nums_dict.get(others)]
        else:
            nums_dict[cur_val] = i


if __name__ == '__main__':
    """
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1]
    """
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
    print(twoSum2(nums, target))
