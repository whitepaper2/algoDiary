#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 下午2:39
# @Author  : pengyuan.li
# @Site    : 
# @File    : 027_remove_element.py
# @Software: PyCharm


def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    else:
        start = 0
        end = len_nums
        while start < end:
            if nums[start] != val:
                start = start + 1
            else:
                end = end-1
                nums[start] = nums[end]
        return end


if __name__ == "__main__":
    """
    remove the val in the list
    """
    # print("test 1")
    # nums = [3, 3]
    # val = 3
    # len_nums = remove_element(nums, val)
    # for i in range(len_nums):
    #     print(nums[i])
    # print("test 2")
    # nums = [3, 2, 2, 3]
    # val = 3
    # len_nums = remove_element(nums, val)
    # for i in range(len_nums):
    #     print(nums[i])
    # print("test 3")
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2
    # len_nums = remove_element(nums, val)
    # for i in range(len_nums):
    #     print(nums[i])
    # print("test 4")
    # nums = [4, 5]
    # val = 4
    # len_nums = remove_element(nums, val)
    # for i in range(len_nums):
    #     print(nums[i])
    haystack = "hello"
    needle = "d"
    print(haystack.find(needle))
    try:
        out = haystack.index(needle)
    except:
        out = -1
    print(out)
