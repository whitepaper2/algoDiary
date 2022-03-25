#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/24 14:23:51
@Author  : pengyuan.li
@File    : 4.7.1-strs.py
@Software: VSCode
'''

# here put the import lib


# 字符串匹配：主串T中匹配模式串S，输出位置
def strMatch(T, S):
    """
    暴力解法，逐个字符匹配
    """
    res = []
    m, n = len(T), len(S)
    for i in range(m - n + 1):
        j = 0
        while j < n and T[i + j] == S[j]:
            j += 1
        if j == n:
            res.append(i)
    return res


# 字符串匹配：主串T中匹配模式串S，输出位置
def strMatch2(T, S):
    """
    暴力解法，逐个字符匹配，计算每个模式串长度的hash值，少了模式串的循环
    """
    m, n = len(T), len(S)
    shash = getstrRangeHash(S, 0, n - 1)
    res = []
    for i in range(m - n + 1):
        thash = getstrRangeHash(T, i, i + n - 1)
        if shash == thash and T[i:i + n] == S:
            res.append(i)
    return res


def getstrHash(S):
    """
    字符串S的hash值，多项式表示 a + b*x + c*x^2
    """
    Mod = 100000007
    b = 233
    res = 0
    c = 1
    for s in S:
        res = (res + ord(s) * c) % Mod
        c = (c * b) % Mod
    return res


def getstrHash2(S):
    """
    字符串S的hash值，多项式表示 a*x^2 + b*x + c
    """
    Mod = 100000007
    b = 233
    res = 0
    for s in S:
        res = (res * b + ord(s)) % Mod
    return res


def getstrPrefixHash(S):
    """
    字符串前缀子串的hash值
    """
    n = len(S)
    Mod = 100000007
    b = 233
    preHash = [0] * n
    B = [1] * n
    c = 0
    for i, s in enumerate(S):
        if i > 0:
            B[i] = (B[i - 1] * b) % Mod
        preHash[i] = (c * b + ord(s)) % Mod
        c = preHash[i]
    return preHash, B


def getstrRangeHash(S, l, r):
    """
    字符串任意子串的hash值，通过前缀串可求任意子串
    """
    preHash, B = getstrPrefixHash(S)
    Mod = 100000007
    return preHash[r] if l == 0 else (preHash[r] -
                                      B[r - l + 1] * preHash[l - 1]) % Mod


def querystrRangeHash(S, queries):
    """
    查询一系列区间的hash值
    """
    res = []
    for l, r in queries:
        res.append(getstrRangeHash(S, l, r))
    return res


# 最大长度回文子串
def getMaxPalidrom(S):
    """
    hash+二分查找
    """
    preHash1, B1 = getstrPrefixHash(S)
    preHash2, B2 = getstrPrefixHash(S[-1::-1])

    def getRangeHash(preHash, B, l, r):
        """
        字符串任意子串的hash值，通过前缀串可求任意子串
        """
        Mod = 100000007
        return preHash[r] if l == 0 else (preHash[r] -
                                          B[r - l + 1] * preHash[l - 1]) % Mod

    def binarySearch(l, r, n, i, isEven):
        """
        [l,r]查找最长回文子串
        """
        while l < r:
            mid = (l + r) // 2
            h1l, h1r = i - mid + isEven, i
            h2l, h2r = n - 1 - (i + mid), n - 1 - (i + isEven)
            h1 = getRangeHash(preHash1, B1, h1l, h1r)
            h2 = getRangeHash(preHash2, B2, h2l, h2r)
            if h1 != h2:
                r = mid
            else:
                l = mid + 1
        return l - 1

    res = 0
    n = len(S)
    # 奇数
    for i in range(n):
        maxLen = min(i, n - i - 1) + 1
        k = binarySearch(0, maxLen, n, i, 0)
        res = max(res, 2 * k + 1)
    # 偶数
    for i in range(n):
        maxLen = min(i + 1, n - i - 1) + 1
        k = binarySearch(0, maxLen, n, i, 1)
        res = max(res, 2 * k)
    return res


def getMaxPalidrom2(S):
    """
    动态规划（当然还有暴力解法），dp[i,j] = 1 if dp[i+1,j-1] and S[i]==S[j] else 0
    """
    n = len(S)
    dp = [[0] * n for _ in range(n)]
    res = 0
    l, r = 0, 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = 1 if dp[i + 1][j - 1] and S[i] == S[j] else 0
            if dp[i][j] and j - i + 1 > res:
                res = j - i + 1
                l, r = i, j
    return res, S[l:r + 1]


if __name__ == "__main__":
    T = "abcabcd"
    S = "ab"
    print(strMatch(T, S))
    print(strMatch2(T, S))

    print(getstrHash(T) == getstrHash2(T[-1::-1]))
    print(getstrRangeHash(T, 1, 3))

    S = "babad"
    print(getMaxPalidrom2(S))
    print(getMaxPalidrom(S))
