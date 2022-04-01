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


def strMatch2(S, T):
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
    m, n = len(S), len(T)
    st = T + '#' + S
    next = getNext2(st)
    for i in range(n, m + n + 1):
        if next[i] == n:
            res.append(i - 2 * n)
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


# 统计每个前缀在字符串中出现的次数，分2种情况
# 1.S的每个前缀与S匹配，求匹配个数
# 2.S的每个前缀与T匹配，求匹配个数
def prefixCnts(S):
    """每个前缀与S匹配，求匹配个数，包括空集
    """
    n = len(S)
    next = getNext2(S)
    res = [0] * (n + 1)
    for i in range(n):
        res[next[i]] += 1
    for i in range(n - 1, 0, -1):
        res[next[i - 1]] += res[i]
    for i in range(n + 1):
        res[i] += 1
    return res


# 本质不同的子串个数，即删除重复子串
def substrNum(S):
    n = len(S)
    res = 0
    for i in range(n):
        cur = S[0:i]
        t = S[i::-1]
        next = getNext2(t)
        res += len(cur) + 1 - max(next)
    return res


def strCompress(S):
    n = len(S)
    next = getNext2(S)
    k = n - next[-1]
    return k if k < n and n % k == 0 else -1


def automation(S):
    """
    ac自动机是一种算法，多模匹配算法，KMP和trie的结合
    """
    pass


if __name__ == "__main__":
    s = "abcabcd"
    t = "ab"
    print(strMatch(s, t))
    print(strMatch2(s, t))

    print(getNext(s))
    print(getNext2(s))

    print(prefixCnts(s))

    print(substrNum(s))
    print(strCompress(s))
