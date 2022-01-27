#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/01/27 14:37:37
@Author  : pengyuan.li
@File    : 4.2.1-gameWin.py
@Software: VSCode
'''

# here put the import lib
from typing import List


def gameWin(N: int, A: List[int]) -> bool:
    """
    ——————————双方都取最优策略，只讨论必须胜或输状态————————————
    当前有j个硬币时，若j=0，Alice必输
    否则，分两种情况讨论
    若存在i,使得j-A[i]必输，j必胜（Alice取出A[i],Bob必输）；
    若任意i,使得j-A[i]必胜，j必输（Alice无论取出哪个A[i],Bob必胜）
    """
    win = [False] * (N + 1)
    win[0] = False
    for i in range(1, N + 1):
        for v in A:
            win[i] |= i >= v and not win[i - v]
    return win[N]


def eulidGame(a, b):
    """
    较大的数字减去较小数字的倍数
    b-a>a:可选a的倍数,存在两种情况，1整除，Alice赢；2不能整除
    b-a<a:没的选择
    """
    res = True
    while True:
        if a > b:
            a, b = b, a
        if b % a == 0:
            break
        if b - a > a:
            break
        b -= a
        res = not res
    return res


if __name__ == "__main__":
    n = 10
    nums = [1, 4]
    print(gameWin(n, nums))

    n = 9
    nums = [1, 4]
    print(gameWin(n, nums))

    a, b = 34, 12
    print(eulidGame(a, b))
    a, b = 15, 24
    print(eulidGame(a, b))
