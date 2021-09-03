#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午7:10
# @Author  : pengyuan.li
# @Site    : 
# @File    : 029_divide.py
# @Software: PyCharm
import sys


def divide(dividend, divisor):
    """
    note: 整除求得商，不得使用乘法、除法和取余操作。
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    m = abs(dividend)
    n = abs(divisor)
    res = 0

    while m >= n:
        t = n
        p = 1
        while m >= (t << 1):
            t <<= 1
            p <<= 1
        res += p
        m -= t
    if (dividend > 0 > divisor) or (dividend < 0 < divisor):
        res = -1*res
    return res


if __name__ == "__main__":
    dividend = -10
    divisor = 3
    print(divide(dividend, divisor))
    # print(int("inf"))
    print(sys.maxsize)
    print(float("inf"))
