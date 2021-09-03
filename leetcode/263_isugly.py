#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 下午7:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 263_isugly.py
# @Software: PyCharm


def isUgly(num: int) -> bool:
    """
    判断一个数是否能被[2,3,5]整除，方法：不停地使用这次数字去除，余数=1则是，否则不是
    :param num: >=1的数字
    :return:true/false
    """
    if num <= 0:
        return False
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5
    return num == 1


def isUgly2(num: int) -> bool:
    """
    判断一个数是否能被[2,3,5]整除，方法：不停地使用这次数字去除，余数=1则是，否则不是
    :param num: >=1的数字
    :return:true/false
    """
    if num <= 0:
        return False
    while num >= 2:
        if num % 2 == 0:
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
        elif num % 5 == 0:
            num = num / 5
        else:
            return False
    return num == 1


if __name__ == "__main__":
    print(isUgly2(8))
    print(isUgly2(14))
    print(isUgly2(6))
