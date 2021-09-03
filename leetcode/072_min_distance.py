#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 下午4:06
# @Author  : pengyuan.li
# @Site    : 
# @File    : 072_min_distance.py
# @Software: PyCharm


def minDistance(word1: str, word2: str) -> int:
    """
    word1->word2通过delete\insert\replace变换得到，dp[i][j]表示word1前i个字符变换到word2前j个字符所需的最少变换个数
    if word1[i]=word2[j]不需要变换, dp[i][j]=dp[i-1][j-1]
    else 1+min(deleteCnt, insertCnt, replaceCnt)
    :param word1: 字符串1
    :param word2: 字符串2
    :return: int
    """
    m = len(word1)
    n = len(word2)
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dist[i][0] = i
    for i in range(1, n + 1):
        dist[0][i] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(min(dist[i - 1][j], dist[i][j - 1]), dist[i - 1][j - 1]) + 1
    return dist[m][n]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))
