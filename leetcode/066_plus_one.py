#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 下午2:06
# @Author  : pengyuan.li
# @Site    : 
# @File    : 066_plus_one.py
# @Software: PyCharm


def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    len_digits = len(digits)
    if len_digits > 1 and digits[0] == 0:
        return 0
    temp_digits = 0
    for i in range(len_digits):
        temp_digits = temp_digits * 10 + digits[i]
    temp_digits = temp_digits + 1
    out = []
    while temp_digits > 0:
        res_digit = temp_digits % 10
        int_digit = int(temp_digits / 10)
        temp_digits = int_digit
        out.append(res_digit)
    out.reverse()
    return out


def plus_one2(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    len_digits = len(digits)
    if len_digits > 1 and digits[0] == 0:
        return 0
    i = len_digits - 1
    while i >= 0 and digits[i] == 9:
        digits[i] = 0
        i = i - 1
    if i == -1:
        digits.insert(0, 1)
    else:
        digits[i] = digits[i] + 1
    return digits


if __name__ == "__main__":
    """
    note: method1 在数值较大时输出结果出错，method2 遇到9进一位
    """
    digits = [1, 2, 3, 4]
    print(plus_one2(digits))
    digits = [9, 9]
    print(plus_one2(digits))
    digits = [0, 9]
    print(plus_one2(digits))
    digits = [0]
    print(plus_one2(digits))
    digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]
    print(plus_one2(digits))

