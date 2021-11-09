#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 上午11:40
# @Author  : pengyuan.li
# @Site    : 
# @File    : 0x33-coresidual.py
# @Software: PyCharm


def equaltion(a, b, c):
    """
    求方程 a*x + b*y = c，解(x,y)
    :param a:
    :param b:
    :param c:
    :return:
    """
    x = 1
    y = 1

    def exgcd(a, b):
        """
        扩展的最大公约数，使用辗转相除法求解
        gcd(a,b) = a*x + b*y
        :param a:
        :param b:
        :return:
        """
        nonlocal x, y
        if b == 0:
            x = 1
            y = 0
            return a
        d = exgcd(b, a % b)
        x, y = y, x - y * (a // b)
        return d

    d = exgcd(a, b)
    if c % d == 0:
        for k in range(1, 5):
            print((x * c + k * b) // d, (c * y - k * a) // d)
    else:
        print("no answer")


def equaltion2(a, b):
    """
    求方程 a*x==1(mod b)
    a*x + b*y = 1，解(x,y)
    :param a:
    :param b:
    :param c:
    :return:
    """
    x = 1
    y = 1

    def exgcd(a, b):
        """
        扩展的最大公约数，使用辗转相除法求解
        gcd(a,b) = a*x + b*y
        :param a:
        :param b:
        :return:
        """
        nonlocal x, y
        if b == 0:
            x = 1
            y = 0
            return a
        d = exgcd(b, a % b)
        x, y = y, x - y * (a // b)
        return d

    d = exgcd(a, b)
    print(x, y, d)
    # 结果保持在[0,b)范围内
    return (x % b + b) % b


def gcd(a, b):
    """
    最大公约数
    :param a:
    :param b:
    :return:
    """
    return a if b == 0 else gcd(b, a % b)


import math


def equaltion3(a, b, p):
    """
    求方程 a^x==b(mod p), gcd(a,p)=1
    解(x)
    :param a:
    :param b:
    :param p:
    :return:
    """

    def mypower(a, x):
        res = 1
        for i in range(x):
            res = res * a
        return res

    t = int(math.sqrt(p)) + 1
    bdict = dict()
    curA = 1
    for j in range(t):
        bdict[b * curA] = j
        curA = curA * a
    tmpA = mypower(a, t)
    if tmpA == 0:
        return 1 if b == 0 else -1
    for i in range(t + 1):
        val = mypower(a, i)
        j = -1 if val not in bdict else bdict[val]
        if j >= 0 and i * t - j >= 0:
            return i * t - j


if __name__ == "__main__":
    # equaltion(5, 8, 10)
    # print(gcd(5, 8))
    # print(equaltion2(5, 8))
    print(equaltion3(3, 2, 7))
