#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/29 17:40:32
@Author  : pengyuan.li
@File    : 0x15-kmp.py
@Software: VSCode
'''


# here put the import lib
# O(n)解决两字符串匹配问题
def strMatch(S, T):
    """
    模式T在字符串S中的匹配位置
    Arguments
    ---------
    S:str
    T:str
    Returns
    -------
    List[int]
    """
    res = []
    next = getNext2(T)
    tar = 0
    pos = 0
    while tar < len(S):
        if S[tar] == T[pos]:
            tar += 1
            pos += 1
        elif pos:
            pos = next[pos - 1]
        else:
            tar += 1
        if pos == len(T):
            res.append(tar - pos)
            pos = next[pos - 1]
    return res


def getNext(S):
    """
    next[i] = max(S[i-j+1:i]==S[1:j])，朴素算法 O(n^2)
    Arguments
    ---------
    S:str
    Returns
    -------
    List[int]
    """
    n = len(S)
    next = [0] * n
    for i in range(1, n):
        for j in range(i, -1, -1):
            if S[0:j] == S[i - j + 1:i + 1]:
                next[i] = j
                break
    return next


def getNext2(S):
    """
    next[i] = max(S[i-j+1:i]==S[1:j])，朴素算法 O(n^2)
    Arguments
    ---------
    S:str
    Returns
    -------
    List[int]
    """
    n = len(S)
    next = [0] * n
    for i in range(1, n):
        j = next[i - 1]
        while j > 0 and S[i] != S[j]:
            j = next[j - 1]
        if S[i] == S[j]:
            j += 1
        next[i] = j
    return next


if __name__ == "__main__":
    s = "abcabcd"
    t = "ab"
    print(strMatch(s, t))

    print(getNext(s))
    print(getNext2(s))
