#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 下午10:40
# @Author  : pengyuan.li
# @Site    : 
# @File    : 007_reverse_number.py
# @Software: PyCharm


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x_out = []
    is_negative = False
    if x == 0:
        out = 0
    else:
        if x < 0:
            x = abs(x)
            is_negative = True
        num = 0
        while x >= 1:
            num = num + 1
            x_res = x % 10
            x_int = int(x / 10)
            x = x_int
            x_out.append(x_res)
        out = x_out[0]
        if num > 1:
            for i in range(num - 1):
                out = out * 10 + x_out[i + 1]
                if out > pow(2, 31) - 1:
                    out = 0
                    break
        if is_negative:
            out = -1 * out
    return out


if __name__ == '__main__':
    """
    Given nums = 123, return 321
    Given nums = -123, return -321
    Given nums = 120, return 21
    if out not in [-pow(2,31),pow(2,31)-1], return 0
    """
    nums = 123
    print(reverse(nums))
    nums = -123
    print(reverse(nums))
    nums = 120
    print(reverse(nums))
