#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 下午7:58
# @Author  : pengyuan.li
# @Site    : 
# @File    : 077_combine.py
# @Software: PyCharm


def combine(n, k):
    """
    note: 根据递推公式，C(n,k)=C(n-1,k)+C(n-1,k-1)
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    def sub_combine(n, k):
        if k > n or k < 0:
            return []
        if k == 0:
            return [[]]
        n1k1 = sub_combine(n - 1, k - 1)
        for i in n1k1:
            i.append(n)
        n1k = sub_combine(n - 1, k)
        for j in n1k:
            n1k1.append(j)
        return n1k1

    return sub_combine(n, k)


if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))
