#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午2:15
# @Author  : pengyuan.li
# @Site    : 
# @File    : 011_max_area.py
# @Software: PyCharm


def max_area(height):
    """
    note: Time limited exceed，两层遍历。
    :type height: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            res = max((j - i) * min(height[i], height[j]), res)
    return res


def max_area2(height):
    """
    note: 桶的盛水量和最短板有关。
    :type height: List[int]
    :rtype: int
    """
    res = 0
    len_height = len(height)
    i = 0
    j = len_height - 1
    while i < j:
        res = max((j - i) * min(height[i], height[j]), res)
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1
    return res


def max_area3(height):
    """
    note: 桶的盛水量和最短板有关。对于相同的桶高度直接跳过。
    :type height: List[int]
    :rtype: int
    """
    res = 0
    len_height = len(height)
    i = 0
    j = len_height - 1
    while i < j:
        h = min(height[i], height[j])
        res = max((j - i) * h, res)
        while i < j and height[i] == h:
            i = i + 1
        while i < j and height[j] == h:
            j = j - 1
    return res


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area3(height))
