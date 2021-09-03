#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 下午7:54
# @Author  : pengyuan.li
# @Site    : 
# @File    : 046_permute.py
# @Software: PyCharm


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    from copy import deepcopy

    def my_swap(ai, aj):
        tmp = nums[aj]
        nums[aj] = nums[ai]
        nums[ai] = tmp

    def permute_dfs(nums, start, out):
        if start >= len(nums):
            out.append(deepcopy(nums))
        i = start

        while i < len(nums):
            my_swap(i, start)
            permute_dfs(nums, start + 1, out)
            my_swap(i, start)
            i = i + 1

    permute_dfs(nums, 0, out)
    return out


def permute2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    from copy import deepcopy

    def permute_dfs(nums, cur_out, out):
        nums = deepcopy(nums)
        if 0 == len(nums):
            out.append(deepcopy(cur_out))
        for i in range(len(nums)):
            cur_out.append(nums[i])
            permute_dfs(nums[:i] + nums[i + 1:], cur_out, out)
            cur_out.pop()

    permute_dfs(nums, [], out)
    return out


def permute3(out, A, start):
    if len(A) == start:
        out.append(list(A))
    else:
        for i in range(start, len(A)):
            A[i], A[start] = A[start], A[i]
            permute3(out, A, start + 1)
            A[i], A[start] = A[start], A[i]


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute2(nums))
    out = list()
    permute3(out, nums, 0)
    print(out)
