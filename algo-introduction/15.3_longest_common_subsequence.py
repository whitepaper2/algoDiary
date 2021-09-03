#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def lcs(X, Y):
    """
    相同的最长字符串，c[i,j]=c[i-1,j-1]+1, X[i]==Y[j]
    c[i,j]=max(c[i-1,j],c[i,j-1]，X[i]!=Y[j]
    :param X:
    :param Y:
    :return:
    """
    m = len(X)
    n = len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    p = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                p[i][j] = "tri"
            else:
                if c[i - 1][j] > c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    p[i][j] = "top"
                else:
                    c[i][j] = c[i][j - 1]
                    p[i][j] = "left"
    print(c)
    return c[m][n], p


def memoLcs(X, Y):
    """
    带备忘本的最长公共子序列
    :param X:
    :param Y:
    :return:
    """
    m, n = len(X), len(Y)
    C = [[0] * (n + 1) for _ in range(m + 1)]

    def subLcs(X, Y, i, j, C):
        if C[i][j] > -1:
            return C[i][j]
        if i == 0 or j == 0:
            return 0

        res = subLcs(X, Y, i - 1, j - 1, C) + 1 if X[i - 1] == Y[j - 1] else max(subLcs(X, Y, i - 1, j, C),
                                                                                 subLcs(X, Y, i, j - 1, C))

        C[i][j] = res

        return res

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            C[i][j] = -1
            subLcs(X, Y, i, j, C)
    print(C)
    return C[m][n]


def printLCS(p, X, m, n):
    """
    打印出共同的最长字符串
    :param p: 记录的路径
    :param X:
    :param m: x.length
    :param n: y.length
    :return:
    """
    if m == 0 or n == 0:
        return
    if p[m][n] == "tri":
        print(X[m - 1])
        printLCS(p, X, m - 1, n - 1)
    elif p[m][n] == "left":
        printLCS(p, X, m, n - 1)
    else:
        printLCS(p, X, m - 1, n)


if __name__ == "__main__":
    x = "ABCBDAB"
    y = "BDCABA"
    l, c = lcs(x, y)
    print(l)
    printLCS(c, x, len(x), len(y))
    print(memoLcs(x, y))
