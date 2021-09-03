#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 上午9:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 078_subsets.py
# @Software: PyCharm


def subsets(nums):
    """
    note: 不相同的数据任意组合 = C(n,0)+C(n,1)+...+C(n,n)，而在计算组合时，重复计算很多次
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def sub_combine(nums, n, k):
        if k > n or k < 0:
            return []
        if k == 0:
            return [[]]
        n1k1 = sub_combine(nums, n - 1, k - 1)
        for i in n1k1:
            i.append(nums[n - 1])
        n1k = sub_combine(nums, n - 1, k)
        for j in n1k:
            n1k1.append(j)
        return n1k1

    out = []
    for i in range(len(nums) + 1):
        out.extend(sub_combine(nums, len(nums), i))
    return out


def subsets2(nums):
    """
    note: 结果是升序排序，首先对原数据排序，第k次结果 = 第k-1次结果 + 第k-1次结果中每个元素加上k。此处list使用deepcopy，数据和地址都复制，其他常用赋值都是浅复制
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from copy import deepcopy
    sort_nums = sorted(nums)
    out = [[]]
    for i in range(len(sort_nums)):
        temp = deepcopy(out)
        for t in temp:
            t.append(sort_nums[i])
        out.extend(temp)
    return out


def subsets3(nums):
    """
    note: 结果是升序排序，首先对原数据排序，DFS遍历二叉树。此处list使用deepcopy，数据和地址都复制，其他常用赋值都是浅复制
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    from copy import deepcopy

    def sub_func(nums, n, k, cur_out):
        if k == n:
            out.append(deepcopy(cur_out))
            return
        # 加入第k元素
        cur_out.append(nums[k])
        sub_func(nums, n, k + 1, cur_out)
        # 不加入第k元素
        cur_out.pop()
        sub_func(nums, n, k + 1, cur_out)

    sub_func(nums, len(nums), 0, [])
    return out


if __name__ == "__main__":
    nums = [5, 8, 9, 10]
    print(subsets3(nums))

    nums = [1, 2, 3]
    print(subsets3(nums))
