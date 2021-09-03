#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 下午7:13
# @Author  : pengyuan.li
# @Site    : 
# @File    : 038_count_say.py
# @Software: PyCharm

from common import timeit


@timeit
def count_say(n):
    """
    note: Given for "1211", record the number of 1 until changed, return num+num[i]
    :type n: int
    :rtype: str
    """
    if n <= 0:
        return ""
    out = "1"
    for i in range(n - 1):
        len_out = len(out)
        cur = []
        # 必须要使用list清除原值
        cur.clear()
        j = 0
        while j < len_out:
            cnt = 1
            while j + 1 < len_out and out[j] == out[j + 1]:
                j = j + 1
                cnt = cnt + 1
            cur.append(str(cnt))
            cur.append(out[j])
            j = j + 1
        out = cur
    return "".join(out)


@timeit
def count_say2(n):
    """
    note: I don't understand regular expression?
    :type n: int
    :rtype: str
    """
    import re
    out = "1"
    for i in range(n - 1):
        out = re.sub(r'(.)\1*', lambda g: str(len(g.group(0))) + g.group(1), out)
    return out


if __name__ == "__main__":
    """
    note: method1 is so faster than method2, but why?
    """
    n = 10
    print(count_say(n))
    print(count_say2(n))


