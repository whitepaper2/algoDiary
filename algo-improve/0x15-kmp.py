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
    KMP解法，1.模式串S的next数组，2.T中匹配next
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
    KMP解法，模式串S的next数组,已知next[0~i-1],求next[i]
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


def strPeriods(S):
    """
    return (len,前缀串(len>1)中的最小循环单元个数)
    """
    n = len(S)
    next = getNext2(S)
    res = []
    for i in range(1, n):
        j = i+1
        if j % (j - next[i]) == 0 and j // (j- next[i]) > 1:
            res.append([j, j // (j- next[i])])
    return res


# 统计每个前缀在字符串中出现的次数，分2种情况
# 1.S的每个前缀与S匹配，求匹配个数
# 2.S的每个前缀与T匹配，求匹配个数
def prefixCnts(S):
    """
    每个前缀与S匹配，求匹配个数，包括空集
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


def miniStrDesc(S):
    """
    字符串的最小表示，即字典序最小的循环同构字符串。
    """
    n = len(S)
    i, j = 0, 1
    k = 0
    while i < n and j < n and k < n:
        if S[(i + k) % n] == S[(j + k) % n]:
            k += 1
        else:
            if S[(i + k) % n] > S[(j + k) % n]:
                i += 1 + k
            else:
                j += 1 + k
            k = 0
            if i == j:
                i += 1
    p = min(i, j)
    return i, S[p:] + S[0:p]


def constructSA(S):
    """
    构造字符串的后缀数组
    """

    pass


def zAlgo(S):
    """
    z-algorithm，扩展KMP，z[i]=LCP(s,s[i,n-1])，字符串与后缀子串的公共前缀，特别地z[0]=0
    三种算法：朴素算法，二分+hash，KMP
    """
    n = len(S)
    z = [0] * n
    for i in range(1, n):
        while i + z[i] < n and S[i + z[i]] == S[0 + z[i]]:
            z[i] += 1
    return z


def zAlgo2(S):
    """
    z-algorithm，扩展KMP，z[i]=LCP(s,s[i,n-1])，字符串与后缀子串的公共前缀，特别地z[0]=0
    三种算法：朴素算法，二分+hash，KMP
    """
    n = len(S)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and S[i + z[i]] == S[0 + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def zAlgo3(S):
    """
    z-algorithm，扩展KMP，z[i]=LCP(s,s[i,n-1])，字符串与后缀子串的公共前缀，特别地z[0]=0
    三种算法：朴素算法，二分+hash，KMP
    """
    Mod = 1000000007
    b = 171
    n = len(S)
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * b + ord(S[i - 1])) % Mod
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        p[i] = p[i - 1] * b % Mod
    res = 0
    for i in range(n, 0, -1):
        head = 0
        tail = n - i + 1
        while head < tail:
            mid = (head + tail + 1) >> 1
            h = (f[i + mid - 1] - f[i - 1] * p[mid] % Mod + Mod) % Mod
            if h == f[mid]:
                head = mid
            else:
                tail = mid - 1
        res += head

    return res


if __name__ == "__main__":
    for s in ["aaa","abcd","aabaabaabaab"]:
        print(strPeriods(s))
    s = "adbcabcd"
    t = "ab"
    print(strMatch(s, t))
    print(strMatch2(s, t))

    print(getNext(s))
    print(getNext2(s))

    print(prefixCnts(s))

    print(substrNum(s))
    print(strCompress(s))
    print(miniStrDesc(s))
    s = "aaabaab"
    print(zAlgo(s))
    print(zAlgo2(s))
    print(zAlgo3(s))
