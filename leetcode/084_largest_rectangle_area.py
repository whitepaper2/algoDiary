#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 下午5:49
# @Author  : pengyuan.li
# @Site    : 
# @File    : 084_largest_rectangle_area.py
# @Software: PyCharm

from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """
    输入直方图，输出构成的矩阵面积最大，Time Limited
    :param heights: 直方图高度
    :return: 最大矩阵面积
    """
    if heights is None:
        return 0
    width = len(heights)
    if width == 0:
        return 0
    left_width = [0] * width
    right_width = [0] * width
    for i in range(width):
        cur_val = heights[i]
        left = i - 1
        while left >= 0 and cur_val <= heights[left]:
            left = left - 1
            left_width[i] = left_width[i] + 1
        right = i + 1
        while right < width and cur_val <= heights[right]:
            right = right + 1
            right_width[i] = right_width[i] + 1
    return max([heights[i] * (left_width[i] + right_width[i] + 1) for i in range(width)])


def largestRectangleArea2(heights: List[int]) -> int:
    """
    输入直方图，输出构成的矩阵面积最大，Time Limited
    寻找局部最大值（第i值大于第i+1值），与前面数值形成矩形面积取最大
    :param heights: 直方图高度
    :return: 最大矩阵面积
    """
    if heights is None:
        return 0
    width = len(heights)
    if width == 0:
        return 0
    out = 0
    for i in range(width):
        if i + 1 < width and heights[i] <= heights[i + 1]:
            continue
        minH = heights[i]
        for j in range(i, -1, -1):
            minH = min(minH, heights[j])
            area = minH * (i - j + 1)
            out = max(out, area)
    return out


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea(heights))
    print(largestRectangleArea2(heights))

    heights = [2]
    print(largestRectangleArea(heights))
    print(largestRectangleArea2(heights))
