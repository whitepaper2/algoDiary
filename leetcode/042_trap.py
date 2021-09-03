#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 上午11:26
# @Author  : pengyuan.li
# @Site    : 
# @File    : 042_trap.py
# @Software: PyCharm
from typing import List


def trap(height: List[int]) -> int:
    """
    note: 双指针法，取左右两端较小值，如果在左端，遍历从左向右，如果小于该值，则可以储水，累加，否则重新确定范围。
    :param height:
    :return:
    """
    left = 0
    right = len(height) - 1
    out = 0
    while left < right:
        mn = min(height[left], height[right])
        if height[left] == mn:
            left = left + 1
            while left < right and height[left] < mn:
                out = out + (mn - height[left])
                left = left + 1
        else:
            right = right - 1
            while left < right and height[right] < mn:
                out = out + (mn - height[right])
                right = right - 1
    return out


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))
