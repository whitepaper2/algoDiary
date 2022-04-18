#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/04/15 16:13:47
@Author  : pengyuan.li
@File    : 4.7.3-suffixstr.py
@Software: VSCode
'''

# here put the import lib
# 后缀数组
from copy import deepcopy
from functools import cmp_to_key


def suffixArr(S):
    """
    朴素算法，O(n^2*logn)
    sa后缀数组，rk后缀排名，sa[rk[i]]=rk[sa[i]]=i
    """
    n = len(S)
    suffixDict = {}
    suffixS = []
    for i in range(n):
        suffixDict[S[i:]] = i
        suffixS.append(S[i:])
    suffixS.sort()
    res = []
    for s in suffixS:
        res.append(suffixDict[s])
    return res


def suffixArr2(S):
    """
    优化算法，倍增，O(n*(logn)^2)
    """
    n = len(S)
    rk = [0] * (n << 1)
    sa = [0] * (n)
    for i in range(n):
        sa[i] = i
        rk[i] = ord(S[i]) - ord('a') + 1
        # rk[i] = S[i] # 修改字符串比较大小
    w = 1
    while w < n:
        # cmp_to_key:比较大小用减法，不等式不正确。
        sa.sort(key=cmp_to_key(lambda x, y: rk[x + w] - rk[y + w]
                               if rk[x] == rk[y] else rk[x] - rk[y]))
        oldrk = deepcopy(rk)
        p = 0
        for i in range(n):
            if oldrk[sa[i]] == oldrk[sa[
                    i - 1]] and sa[i] + w < n and sa[i - 1] + w < n and oldrk[
                        sa[i] + w] == oldrk[sa[i - 1] + w]:
                rk[sa[i]] = p
            else:
                p += 1
                rk[sa[i]] = p
        w <<= 1
    return sa


if __name__ == "__main__":
    s = "aabaaaab"
    print(suffixArr(s))
    print(suffixArr2(s))