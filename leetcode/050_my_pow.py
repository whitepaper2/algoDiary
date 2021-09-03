#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 下午6:38
# @Author  : pengyuan.li
# @Site    : 
# @File    : 050_my_pow.py
# @Software: PyCharm


def my_pow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """

    def power(x, n):
        if n == 0:
            return 1
        else:
            half = power(x, int(n / 2))
            out = half * half if n % 2 == 0 else half * half * x
            return out

    out = 1 / power(x, -n) if n < 0 else power(x, n)
    return 1.0 * out


if __name__ == "__main__":
    n = pow(2, 31)
    print(n)
    print(my_pow(100, 2))
    # print(pow(100.0, 1000))
