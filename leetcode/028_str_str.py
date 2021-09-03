#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 下午6:51
# @Author  : pengyuan.li
# @Site    : 
# @File    : 028_str_str.py
# @Software: PyCharm


def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)


def str_str2(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    len_haystack = len(haystack)
    len_needle = len(needle)
    if len_needle == 0:
        return 0
    if len_haystack < len_needle:
        return -1
    for i in range(len_haystack - len_needle + 1):
        j = 0
        while j < len_needle:
            if haystack[i + j] != needle[j]:
                break
            j = j + 1
        if j == len_needle:
            return i
    return -1


if __name__ == "__main__":
    """
    method1 is so faster than method2
    """
    haystack = "hello"
    needle = "ll"
    print(str_str2(haystack, needle))
