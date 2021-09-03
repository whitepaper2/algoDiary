#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 下午7:50
# @Author  : pengyuan.li
# @Site    : 
# @File    : 263_isugly.py
# @Software: PyCharm
import heapq


def nthUglyNumber(n: int) -> int:
    """
    遍历每个数值，判断是否为丑数
    :param n: 输出第n个丑数
    :return:
    """
    i = 1
    cnt = 0
    while True:
        if isUgly(i):
            cnt = cnt + 1
        if cnt == n:
            break
        i = i + 1
    return i


def nthUglyNumber2(n: int) -> int:
    """
    丑数*丑数=丑数，维护三个数组m2\m3\m5，每次取min(m2,m3,m5)加入丑数集合，这三个数组更新规则：小于刚加入的丑数则+1
    :param n: 输出第n个丑数
    :return:
    """
    i2 = 0
    i3 = 0
    i5 = 0
    out = [1]
    cnt = 0
    while cnt < n - 1:
        m2 = out[i2] * 2
        m3 = out[i3] * 3
        m5 = out[i5] * 5
        mn = min(m2, min(m3, m5))
        out.append(mn)
        if mn == m2:
            i2 = i2 + 1
        if mn == m3:
            i3 = i3 + 1
        if mn == m5:
            i5 = i5 + 1
        cnt = cnt + 1
    return out[-1]


def nthUglyNumber3(n: int) -> int:
    """
    丑数*丑数=丑数，维护一个最小堆，每次取出堆头元素，同时删除与此元素相同的元素，最后返回堆头元素
    :param n: 输出第n个丑数
    :return:
    """
    heap = []
    heapq.heappush(heap, 1)
    for i in range(n-1):
        t = heapq.heappop(heap)
        while len(heap) != 0 and t == heap[0]:
            t = heapq.heappop(heap)
        heapq.heappush(heap, t * 2)
        heapq.heappush(heap, t * 3)
        heapq.heappush(heap, t * 5)
    return heap[0]


def isUgly(num: int) -> bool:
    """
    判断一个数是否能被[2,3,5]整除，方法：不停地使用这次数字去除，余数=1则是，否则不是
    :param num: >=1的数字
    :return:true/false
    """
    if num <= 0:
        return False
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5
    return num == 1


def isUgly2(num: int) -> bool:
    """
    判断一个数是否能被[2,3,5]整除，方法：不停地使用这次数字去除，余数=1则是，否则不是
    :param num: >=1的数字
    :return:true/false
    """
    if num <= 0:
        return False
    while num >= 2:
        if num % 2 == 0:
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
        elif num % 5 == 0:
            num = num / 5
        else:
            return False
    return num == 1


if __name__ == "__main__":
    print(nthUglyNumber3(8))
    print(nthUglyNumber3(10))
    print(nthUglyNumber3(2))
    print(nthUglyNumber2(1000))
    print(isUgly2(14))
    print(isUgly2(6))
