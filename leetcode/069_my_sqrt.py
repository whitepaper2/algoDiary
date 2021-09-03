#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 下午2:12
# @Author  : pengyuan.li
# @Site    : 
# @File    : 069_my_sqrt.py
# @Software: PyCharm
from common import timeit


def my_sqrt(x):
    """
    note: 该问题可转换为求解二次函数最优解。牛顿迭代法，f(x)=f(x0)+g(x0)*(x-x0),当f(x)=0，沿切线方向下降最快得到最优解
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    x0 = 1
    x1 = x0 - (x0 * x0 - x) / (2 * x0)
    while abs(x1 - x0) > 1e-6:
        x0 = x1
        x1 = x0 - (x0 * x0 - x) / (2 * x0)
    return int(x0)


@timeit
def my_sqrt2(x):
    """
    note: 二分求解法
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    left = 0
    right = x
    while left < right:
        middle = int((left + right) / 2)
        if middle > x / middle:
            right = middle
        else:
            left = middle + 1

    return right - 1


def my_sqrt3(x):
    """
    note: 二分求解法，可以理解成在range(x)中寻找某个数，返回最右边值
    :type x: int
    :rtype: int
    """
    left = 0
    right = x
    while left <= right:
        mid = left + (right-left)//2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return right



if __name__ == "__main__":
    x = 10
    print(my_sqrt3(x))
    x = 1
    print(my_sqrt3(x))
    x = 16
    print(my_sqrt3(x))
    x = 2147395599
    print(my_sqrt2(x))
