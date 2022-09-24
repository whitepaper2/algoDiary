#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/09/24 22:23:22
@Author  : pengyuan.li
@File    : 0x23-cake.py
@Software: VSCode
'''

# here put the import lib
# 制作多层生日蛋糕，体积N，层数M，要求使用的奶油最少
# 范围：1<=N<=10000,1<=M<=20

from math import sqrt


class Cake(object):

    def __init__(self, n, m) -> None:
        self.maxN = 24
        self.res = float('inf')
        self.n = n
        self.m = m
        self.R = [0] * self.maxN
        self.H = [0] * self.maxN
        self.mins = [0] * self.maxN
        self.minv = [0] * self.maxN

        for i in range(1, self.m + 1):
            self.mins[i] = self.mins[i - 1] + 2 * i * i
            self.minv[i] = self.minv[i - 1] + i * i * i
        self.R[self.m + 1] = float('inf')
        self.H[self.m + 1] = float('inf')

    def __dfs(self, u, v, s):
        if v + self.minv[u] > self.n:
            return
        if s + self.mins[u] >= self.res:
            return
        if s + 2 * (self.n - v) / self.R[u + 1] >= self.res:
            return
        if not u:
            if v == self.n:
                self.res = s
            return
        for r in range(
                min(self.R[u + 1] - 1,
                    int(sqrt((self.n - v - self.minv[u - 1]) / u))), u - 1,
                -1):
            for h in range(
                    min(self.H[u + 1] - 1,
                        int((self.n - v - self.minv[u - 1]) / r / r)), u - 1,
                    -1):
                self.H[u] = h
                self.R[u] = r
                t = r * r if u == self.m else 0
                self.__dfs(u - 1, v + r * r * h, s + 2 * r * h + t)

    def minArea(self):
        self.__dfs(self.m, 0, 0)
        return 0 if self.res == float('inf') else self.res


if __name__ == "__main__":
    N, M = 100, 2
    cake = Cake(N, M)
    print(cake.minArea())
