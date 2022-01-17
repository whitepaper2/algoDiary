#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/17 11:37:07
@Author  : pengyuan.li
@File    : double-week68.py
@Software: VSCode
'''

# here put the import lib
"""
2116. 判断一个括号字符串是否有效
一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的：

字符串为 ().
它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。
它可以表示为 (A) ，其中 A 是一个有效括号字符串。
给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。locked 是一个二进制字符串，只包含 '0' 和 '1' 。对于 locked 中 每一个 下标 i ：

如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。
如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。
如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。
"""


def canBeValid(s: str, locked: str) -> bool:
    """奇数返回False
    从左到右，记录不可修改的')'个数k，与配对的i+1-k，i+1-k<k不可匹配
    从右到左，记录不可修改的'('个数k，与配对的n-i-k，n-i-k<k不可匹配
    """
    n = len(s)
    if n % 2 == 1:
        return False
    left, right = 0, 0
    for i in range(n):
        if locked[i] == '1' and s[i] == ')':
            right += 1
            if i + 1 - right < right:
                return False
    for i in range(n - 1, -1, -1):
        if locked[i] == '1' and s[i] == '(':
            left += 1
            if n - i - left < left:
                return False
    return True


if __name__ == "__main__":
    s = "))()))"
    locked = "010100"
    print(canBeValid(s, locked))
