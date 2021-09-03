#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 下午10:34
# @Author  : pengyuan.li
# @Site    : 
# @File    : 118_generate.py
# @Software: PyCharm


def generate(numRows):
    """
    note: 维护一个下三角二维矩阵，第一列和对角线值都为1，a[i][j]=a[i-1][j-1]+a[i-1][j], i>2, 1<j<i
    python 二维list必须先赋值，然后才能修改。
    :type numRows: int
    :rtype: List[List[int]]
    """
    out = []
    for i in range(numRows):
        out.append([1] * (i + 1))
        for j in range(1, i):
            if j == 0 or j == i:
                pass
            else:
                out[i][j] = out[i - 1][j - 1] + out[i - 1][j]
    return out


def generate2(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    out = []
    for i in range(numRows):
        out.append([1] * (i + 1))
        for j in range(1, i):
            out[i][j] = out[i - 1][j - 1] + out[i - 1][j]
    return out


if __name__ == "__main__":
    print(generate(5))
