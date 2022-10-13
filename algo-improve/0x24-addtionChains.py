#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/10/08 21:31:45
@Author  : pengyuan.li
@File    : 0x24-addtionChains.py
@Software: VSCode
'''

# here put the import lib


# 加成序列，迭代加深
class addChains(object):

    def __init__(self) -> None:
        self.maxdepth = 104
        self.visited = [False] * self.maxdepth
        self.chains = [0] * self.maxdepth

    def printChains(self, n):
        d = 1
        self.chains[1] = 1
        while not self._dfs(2, d, n):
            d += 1
        print(self.chains[1:d + 1])

    def _dfs(self, u, d, n):
        if u == d + 1:
            if self.chains[d] == n:
                return True
            else:
                return False
        if (self.chains[u - 1] << (d - u + 1)) < n:
            return False
        if u > d:
            return False
        for j in range(u - 1, 0, -1):
            if self.chains[u - 1] + self.chains[
                    j] < self.maxdepth and not self.visited[self.chains[u - 1]
                                                            + self.chains[j]]:
                self.chains[u] = self.chains[u - 1] + self.chains[j]
                self.visited[self.chains[u]] = True
                if self._dfs(u + 1, d, n):
                    self.visited[self.chains[u]] = False
                    return True
                self.visited[self.chains[u]] = False
        return False


# 最接近target的子集，双向搜索
class biSearch(object):

    def __init__(self, w, g) -> None:
        self.N = 1 << 25
        self.weights = [float('inf')] * self.N
        self.g = g
        self.n = len(self.g)
        self.cnt = 0
        self.res = 0
        self.m = w  # 最大重量
        self.k = self.n >> 1

    def dfs(self, u, s):
        if u == self.k:
            self.weights[self.cnt] = s
            self.cnt += 1
            return
        self.dfs(u + 1, s)
        if s + self.g[u] <= self.m:
            self.dfs(u + 1, s + self.g[u])

    def dfs2(self, u, s):
        if u == self.n:
            l, r = 0, self.cnt - 1
            while l < r:
                mid = (l + r + 1) >> 1
                if self.weights[mid] <= self.m - s:
                    l = mid
                else:
                    r = mid - 1
            self.res = max(self.res, self.weights[l] + s)
            return
        self.dfs2(u + 1, s)
        if s + self.g[u] <= self.m:
            self.dfs2(u + 1, s + self.g[u])
        pass

    def getMaxSubsets(self):
        self.g.sort(reverse=True)
        self.dfs(0, 0)
        self.weights.sort()
        t = 1
        for i in range(1, self.cnt):
            if self.weights[i] != self.weights[i - 1]:
                self.weights[t] = self.weights[i]
                t += 1
        self.cnt = t
        self.dfs2(self.k, 0)
        return self.res


if __name__ == "__main__":
    nums = [5, 7, 12, 15, 77]
    addc = addChains()
    for i in nums:
        addc.printChains(i)

    w, g = 20, [7, 5, 4, 18, 1]
    bi = biSearch(w, g)
    print(bi.getMaxSubsets())
