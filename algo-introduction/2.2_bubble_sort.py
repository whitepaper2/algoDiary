#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm


def iterBubbleSort(nums):
    """
    note: 算法导论-2.2练习题：冒泡排序，升序，每次交换得到最小值
    :param nums: List[Int]
    :return: List[Int]
    """
    for i in range(0, len(nums) - 1):
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def recursiveSub(A, i):
    """
    尾递归，已排序A[0...i-1]+A[i]，每次交换得到最大值
    :param A:
    :param i:
    :return:
    """
    if i <= 0:
        return
    recursiveSub(A, i - 1)
    if A[i - 1] > A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]


def recursiveBubbleSort(nums):
    """
    note: 算法导论-2.2练习题：冒泡排序，升序
    :param nums: List[Int]
    :return: List[Int]
    """
    recursiveSub(nums, len(nums)-1)
    return nums


if __name__ == "__main__":
    nums = [31, 41, 59, 26, 41, 58]
    print(iterBubbleSort(nums))
    print(recursiveBubbleSort(nums))
