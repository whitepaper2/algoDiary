#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 上午11:56
# @Author  : pengyuan.li
# @Site    : 
# @File    : 119_get_row.py
# @Software: PyCharm


def get_row(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    out = []
    for i in range(rowIndex + 1):
        out.append([1] * (i + 1))
        for j in range(i):
            if j == 0:
                pass
            else:
                out[i][j] = out[i - 1][j - 1] + out[i - 1][j]
    return out[rowIndex]


def get_row2(rowIndex):
    """
    note: 空间复杂度 o(k)，在每一层，从后向前计算
    :type rowIndex: int
    :rtype: List[int]
    """
    out = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            out[j] = out[j - 1] + out[j]
    return out


if __name__ == "__main__":
    print(get_row(5))
    print(get_row2(5))
