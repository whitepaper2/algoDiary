#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 下午8:23
# @Author  : pengyuan.li
# @Site    : 
# @File    : 136_single_number.py
# @Software: PyCharm


def single_number(nums):
    """
    note: 维护一个non_list，遍历nums，如果某个元素在non_list中，则把该元素从none_list中删除，否则把该元素加入到non_list
    :type nums: List[int]
    :rtype: int
    """
    non_repeat = []
    for num in nums:
        if num not in non_repeat:
            non_repeat.append(num)
        else:
            non_repeat.remove(num)
    return non_repeat.pop()


def single_number2(nums):
    """
    note:维护一个hashtable，优点是查找速度快，遍历nums，删除每个元素，若存在，则删除，否则添加key
    :type nums: List[int]
    :rtype: int
    """
    non_repeat = {}
    for num in nums:
        try:
            # 删除key=num的键值对
            non_repeat.pop(num)
        except:
            non_repeat[num] = 1
    return non_repeat.popitem()[0]


def single_number3(nums):
    """
    note: 2*(a+b+c)-(a+b+c+a+b) = c
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(list(set(nums))) - sum(nums)


def single_number4(nums):
    """
    note: 异或运算
    :type nums: List[int]
    :rtype: int
    """
    out = 0
    for num in nums:
        out ^= num
    return out


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(single_number4(nums))
    nums = [4, 1, 2, 1, 2]
    print(single_number4(nums))
