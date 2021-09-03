#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 下午4:37
# @Author  : pengyuan.li
# @Site    : 
# @File    : 091_num_decoding.py
# @Software: PyCharm


def numDecodings(s: str) -> int:
    """
    输入字符串，返回不同组合形式
    :param s: 字符串
    :return: int
    """
    if str is None:
        return 0
    n = len(str)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
        if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and int(s[i - 1]) <= 6)):
            dp[i] = dp[i] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    str = "226"
    print(numDecodings(str))
