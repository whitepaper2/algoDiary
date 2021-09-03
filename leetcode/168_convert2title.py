#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 下午2:52
# @Author  : pengyuan.li
# @Site    : 
# @File    : 168_convert2title.py
# @Software: PyCharm

# excel sheet title to number，28->"AB"

from collections import deque


def convert2title(n: int) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n:
        n -= 1
        res = letters[n % 26] + res
        n //= 26
    return res


def convert2title2(n: int) -> str:
    res = deque()
    while n != 0:
        q, r = divmod(n, 26)
        if r == 0:
            q = q - 1
            r = 26
        else:
            pass
        res.appendleft(r)
        n = q
    res = [chr(ord('A') + elem - 1) for elem in res]
    return "".join(res)


if __name__ == '__main__':
    print(convert2title(701))
    print(convert2title2(701))
