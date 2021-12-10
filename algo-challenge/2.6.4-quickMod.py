#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 上午10:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.6.4-quickMod.py
# @Software: PyCharm


"""
判断一个数是否为Carmichael Number,
合数、x^n=x(mod n), 1<x<n
"""


def isCarmichaelNum(n):
    # 1.是否素数
    def isPrime(x):
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    if isPrime(n):
        return 'No'

    # 递归法
    # def getNtimes(a, i, b):
    #     """
    #     a^i(mod b)
    #     :param a:
    #     :param i:
    #     :param b:
    #     :return:
    #     """
    #     if i == 0:
    #         return 1
    #     t = getNtimes(a, i // 2, b)
    #     res = t * t % b
    #     if i % 2 == 1:
    #         return res * a % b
    #     return res
    # 快速幂
    def getNtimes(a, i, b):
        """
        a^i(mod b)
        :param a:
        :param i:
        :param b:
        :return:
        """
        res = 1
        while i > 0:
            if i & 1:
                res = res * a % b
            a = a * a % b
            i >>= 1
        return res

    # 2.模n同余
    def isMod(a, b):
        return getNtimes(a, b, b) == a

    for i in range(2, n):
        if not isMod(i, n):
            return 'No'
    return 'Yes'


if __name__ == "__main__":
    n = 561
    print(isCarmichaelNum(n))
