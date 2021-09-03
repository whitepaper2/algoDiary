#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 上午11:11
# @Author  : pengyuan.li
# @Site    : 
# @File    : 125_is_palindrome.py
# @Software: PyCharm


def is_palindrome(s):
    """
    note: 数值转为字符串，双指针法，维护首尾指针，分别进行判断
    :type s: str
    :rtype: bool
    """
    out = True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].isalnum() is False:
            left = left + 1
            continue
        if s[right].isalnum() is False:
            right = right - 1
            continue
        if s[left].lower() == s[right].lower():
            left = left + 1
            right = right - 1
        else:
            out = False
            break
    return out


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))

    s = "race a car"
    print(is_palindrome(s))
