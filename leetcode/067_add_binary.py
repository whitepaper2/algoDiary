#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 下午8:16
# @Author  : pengyuan.li
# @Site    : 
# @File    : 067_add_binary.py
# @Software: PyCharm


def add_binary(a, b):
    """
    note: not end
    :type a: str
    :type b: str
    :rtype: str
    """
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        temp = a
        a = b
        b = temp
        len_temp = len_a
        len_a = len_b
        len_b = len_temp

    temp_a = [0] * len_b

    temp_b = []
    for i in range(len_a):
        temp_a[len_b - len_a + i] = int(a[i])

    for i in range(len_b):
        temp_b.append(int(b[i]))
    flag = False
    temp_out = []
    for i in range(len_b - 1, -1, -1):
        if flag:
            if temp_a[i] + temp_b[i] == 1:
                temp_out.insert(0, '1')
            else:
                flag = True
                temp_out.insert(0, '0')
        else:
            if temp_a[i] + temp_b[i] == 1:
                flag = False
                temp_out.insert(0, '1')
            else:
                flag = True
                temp_out.insert(0, '0')
    if flag:
        temp_out.insert(0, '1')
    return "".join(temp_out)


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(add_binary(a, b))
