#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 上午9:57
# @Author  : pengyuan.li
# @Site    : 
# @File    : 058_length_last_word.py
# @Software: PyCharm

from common import timeit


@timeit
def length_of_last_word(s):
    """
    :type s: str
    :rtype: int
    """
    len_s = len(s)
    if len_s == 0:
        return 0
    s_arr = s.strip().split(" ")
    return len(s_arr[-1])


@timeit
def length_of_last_word2(s):
    """
    :type s: str
    :rtype: int
    """
    s_arr = s.strip().split(" ")
    return len(s_arr[-1])


if __name__ == "__main__":
    """
    note: 在LeetCode上提交method1更快点？猜测可能是不同测试案例
    """
    s = "Hello World"
    print(length_of_last_word(s))
    s = "Hello World"
    print(length_of_last_word2(s))
    s = "Hello "
    print(length_of_last_word(s))
    s = "Hello  World"
    print(length_of_last_word(s))
    s = ""
    print(length_of_last_word2(s))
