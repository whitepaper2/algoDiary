#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 下午10:32
# @Author  : pengyuan.li
# @Site    : 
# @File    : 070_climb_stairs.py
# @Software: PyCharm


def climb_stairs(n):
    """
    note: 大问题分解为小问题，子解，i(th)=i-1(th)+i-2(th)，保存路径上的值
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return n
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]


def climb_stairs2(n):
    """
    note: 大问题分解为小问题，子解，i(th)=i-1(th)+i-2(th)，fib数
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return n
    dp0 = 1
    dp1 = 2
    for i in range(2, n):
        temp = dp1
        dp1 = dp1 + dp0
        dp0 = temp
    return dp1


if __name__ == "__main__":
    n = 5
    print(climb_stairs(n))
    n = 5
    print(climb_stairs2(n))
