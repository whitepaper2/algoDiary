#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 下午4:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x42-BinaryIndexTree.py
# @Software: PyCharm


def genBinaryIndexTree(x):
    while x > 0:
        print("[{},{}]".format(x - (x & -x) + 1, x))
        x -= x & -x


if __name__ == "__main__":
    x = 100
    genBinaryIndexTree(x)
