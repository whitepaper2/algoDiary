#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 下午6:17
# @Author  : pengyuan.li
# @Site    : 
# @File    : 020_is_valid.py
# @Software: PyCharm


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    out = False
    queue = []
    len_s = len(s)
    if len_s == 0:
        out = True
    else:
        for i in s:
            if i == "(" or i == "[" or i == "{":
                queue.append(i)
            else:
                if len(queue) > 0:
                    temp = queue.pop()
                    if (temp == "(" and i == ")") or (temp == "[" and i == "]") or (temp == "{" and i == "}"):
                        out = True
                    else:
                        queue.append(temp)
                        out = False
                        break
                else:
                    out = False
                    break
        if len(queue) > 0:
            out = False
    return out


if __name__ == "__main__":
    s = "()"
    print(is_valid(s))
    s = "()[]{}"
    print(is_valid(s))
    s = "(]"
    print(is_valid(s))
    s = "([)]"
    print(is_valid(s))
    s = "{[]}"
    print(is_valid(s))
    s = "]"
    print(is_valid(s))
    s = "["
    print(is_valid(s))
    s = ""
    print(is_valid(s))
    s = "([]"
    print(is_valid(s))
