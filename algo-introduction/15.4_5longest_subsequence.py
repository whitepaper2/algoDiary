#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午8:53
# @Author  : pengyuan.li
# @Site    : 
# @File    : 16.1_greedy_activity.py
# @Software: PyCharm


def lcs(X):
    """
    最长单调子序列，X和X的单调序列，再取公共子串
    相同的最长字符串，c[i,j]=c[i-1,j-1]+1, X[i]==Y[j]
    c[i,j]=max(c[i-1,j],c[i,j-1]，X[i]!=Y[j]
    :param X:
    :return:
    """
    m = len(X)
    Y = sorted(X)
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
    return c[m][n], p


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


def dpLCS(A):
    """
    最长单调子序列，dp[i]=max(dp[j])+1,j<i,A[j]<A[i]
    :param A:
    :return:
    """
    n = len(A)
    dp = [1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        # tmp = dp[i]
        for j in range(i - 1, 0, -1):
            if A[j - 1] < A[i - 1] and dp[i] < dp[j] + 1:
                # if tmp < dp[j] + 1:
                #     tmp = dp[j] + 1
                dp[i] = dp[j] + 1
    print(dp)
    return max(dp)


def binSearch(nums, left, right, target):
    mid = (left + right) // 2
    print(mid)
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        right = mid - 1
        return binSearch(nums, left, right, target)
    else:
        left = mid + 1
        return binSearch(nums, left, right, target)
    return -1


nums = [1, 2, 3]


def traceBack(nums, level, cur, out):
    if level == len(nums):
        #     return
        # if level == len(cur):
        out.append(list(cur))
        return
    for j in range(len(nums)):
        # if level != j and nums[j] == nums[j - 1]:
        #     continue
        cur.append(nums[j])
        traceBack(nums, level + 1, cur, out)
        cur.pop()


out = []
level = 0
cur = []
traceBack(nums, level, cur, out)
print(out)
# if __name__ == "__main__":
#     x = "1,7,3,5,9,4,8"
#     y = x.split(',')
#     l, c = lcs(y)
#     print(l)
#     printLCS(c, y, len(y), len(y))
#     print(dpLCS(x.split(',')))
#     print(dpLCS([1]))
