#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 下午10:40
# @Author  : pengyuan.li
# @Site    : 
# @File    : 002_fib.py
# @Software: PyCharm


def fib(n):
    """
    note:1,1,2,3,5,8
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    """
    note:1,1,2,3,5,8
    :param n:
    :return:
    """
    out = [1] * n
    for i in range(2, n):
        out[i] = out[i - 1] + out[i - 2]
    return out[n - 1]


if __name__ == "__main__":
    print(fib(6))
    print(fib2(8))
