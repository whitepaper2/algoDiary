#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 上午11:42
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x61-telephoneLines.py
# @Software: PyCharm


def telephoneLines(N, paths, freeNum):
    """

    :param N: 基站个数
    :param paths: 通信电缆线路
    :param freeNum: 免费升级的线路个数
    :return:
    """
    pass


if __name__ == "__main__":
    N = 5
    paths = [[1, 2, 5],
             [3, 1, 4],
             [2, 4, 8],
             [3, 2, 3],
             [5, 2, 9],
             [3, 4, 7],
             [4, 5, 6]]
    K = 1
    print(telephoneLines(N, paths, K))
