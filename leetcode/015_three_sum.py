#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 下午2:03
# @Author  : pengyuan.li
# @Site    : 
# @File    : 015_three_sum.py
# @Software: PyCharm


def three_sum(nums):
    """
    note：首先对数据进行排序， 遍历数据，固定第一个数据（若相同则跳过，只保留相同数据的第一个数），再后面的数组中维护首尾两个指针，寻找三值和=0
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    len_nums = len(nums)
    sort_nums = sorted(nums)

    i = 0
    while i < len_nums - 2:
        if sort_nums[i] > 0:
            break
        if i > 0 and sort_nums[i] == sort_nums[i - 1]:
            i = i + 1
            continue
        target = -1 * sort_nums[i]
        left = i + 1
        right = len_nums - 1
        while left < right:
            temp = sort_nums[left] + sort_nums[right]
            if target == temp:
                out.append([sort_nums[i], sort_nums[left], sort_nums[right]])
                while left < right and sort_nums[left] == sort_nums[left + 1]:
                    left = left + 1
                while left < right and sort_nums[right] == sort_nums[right - 1]:
                    right = right - 1
                left = left + 1
                right = right - 1
            elif target > temp:
                left = left + 1
            else:
                right = right - 1
        i = i + 1
    return out


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
    nums = [1, 1, -2]
    print(three_sum(nums))
    nums = [1, 0, 0, -1]
    print(three_sum(nums))
    nums = [1, 0, -1, -1]
    print(three_sum(nums))
    nums = [0, 0, 0, 0, -1, -1, 2]
    print(three_sum(nums))
    nums = [-2, 0, 1, 1, 2]
    print(three_sum(nums))
    nums = [0, 0, 0, 0]
    print(three_sum(nums))
