#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 下午10:34
# @Author  : pengyuan.li
# @Site    : 
# @File    : 121_max_profit.py
# @Software: PyCharm


def max_profit(prices):
    """
    note:两层循环遍历，在大数据量下运行超时
    :type prices: List[int]
    :rtype: int
    """
    out = 0
    len_prices = len(prices)
    for i in range(len_prices):
        for j in range(i + 1, len_prices):
            if prices[i] < prices[j]:
                out = prices[j] - prices[i] if prices[j] - prices[i] > out else out
    return out


def max_profit2(prices):
    """
    note:遍历一次数据，记录下目前为止的最小值、输出最大值。
    :type prices: List[int]
    :rtype: int
    """
    out = 0
    m_min = float("inf")
    for i in prices:
        m_min = min(i, m_min)
        out = max(i - m_min, out)
    return out


def max_profit3(prices):
    """
    note:遍历一次数据，记录下目前为止的最大值、输出最大值。
    :type prices: List[int]
    :rtype: int
    """
    out = 0
    max_cur = 0
    for i in range(1, len(prices)):
        max_cur = max(0, max_cur+(prices[i]-prices[i-1]))
        out = max(max_cur, out)
    return out


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit3(prices))

    prices = [7, 6, 4, 3, 1]
    print(max_profit3(prices))
