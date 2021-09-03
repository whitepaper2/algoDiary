#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午2:01
# @Author  : pengyuan.li
# @Site    : 
# @File    : 2.1_2_insertion_sort.py
# @Software: PyCharm

import random


def randomab(a, b):
    """
    返回正整数区间[a,b]内的随机整数，调用random(0,1)
    :param a:
    :param b:
    :return:
    """
    bin_len = len(bin(b)) - 2
    cur_sum = 0
    for i in range(bin_len):
        cur_sum += random.randint(0, 1) << i
    if a <= cur_sum <= b:
        return cur_sum
    return randomab(a, b)


if __name__ == "__main__":
    for i in range(10):
        print(randomab(3, 7))
