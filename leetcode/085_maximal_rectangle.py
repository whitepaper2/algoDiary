#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 下午5:49
# @Author  : pengyuan.li
# @Site    : 
# @File    : 084_largest_rectangle_area.py
# @Software: PyCharm

from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
    """
    求得最大矩形面积，组成直方图
    :param matrix: 元素由0、1组成
    :return: int
    """
    if matrix is None:
        return 0
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    out = 0
    for i in range(m):
        for j in range(n):
            heights[j] = 0 if matrix[i][j] == '0' else (heights[j] + 1)
        out = max(out, largestRectangleArea2(heights))
    return out


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
    matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    print(maximalRectangle(matrix))
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea2(heights))

    heights = [2]
    print(largestRectangleArea2(heights))
