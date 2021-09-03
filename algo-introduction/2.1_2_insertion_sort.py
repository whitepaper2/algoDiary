#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm


def insertion_sort(nums):
    """
    note: 算法导论-2.1-2练习题：插入排序，非升序
    :param nums: List[Int]
    :return: List[Int]
    """
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
    return nums


def recursiveSub(A, i):
    """
    已排序 A[0...i-1]+A[i]
    :param A:
    :param i:
    :return:
    """
    if i <= 0:
        return
    recursiveSub(A, i - 1)
    j = i - 1
    key = A[i]
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key


def recursive_insertion_sort(nums):
    """
    note: 递归版插入排序，升序
    :param nums: List[Int]
    :return: List[Int]
    """
    recursiveSub(nums, len(nums) - 1)
    return nums


if __name__ == "__main__":
    nums = [31, 41, 59, 26, 41, 58]
    print(insertion_sort(nums))
    print(recursive_insertion_sort(nums))
