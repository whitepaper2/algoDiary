#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 上午9:15
# @Author  : pengyuan.li
# @Site    : 
# @File    : 009_is_palindrome.py
# @Software: PyCharm


def is_palindrome(x):
    """
    note:对数字进行元素抽取，再取前半部分元素逐一与后面元素相比较
    :type x: int
    :rtype: bool
    """
    x_out = []
    out = True
    if x < 0:
        out = False
    else:
        while x >= 1:
            x_res = x % 10
            x_int = int(x / 10)
            x = x_int
            x_out.append(x_res)
        len_xout = len(x_out)
        for i in range(int(len_xout / 2)):
            if x_out[i] != x_out[len_xout - i - 1]:
                out = False
    return out


def is_palindrome2(x):
    """
    note: 数值转为字符串，双指针法，维护首尾指针，分别进行判断
    :type x: int
    :rtype: bool
    """
    out = True
    x_str = str(x)
    left = 0
    right = len(x_str) - 1
    while left < right:
        if x_str[left] == x_str[right]:
            left = left + 1
            right = right - 1
        else:
            out = False
            break
    return out


if __name__ == "__main__":
    """
    Given x = 121, return True
    Given x = -121, return False
    Given x = 120, return False
    """
    print(is_palindrome(0))
    print(is_palindrome(121))
    print(is_palindrome(-121))
    print(is_palindrome(120))

    print(is_palindrome2(0))
    print(is_palindrome2(121))
    print(is_palindrome2(-121))
    print(is_palindrome2(120))
