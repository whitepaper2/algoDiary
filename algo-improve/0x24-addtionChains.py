#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/10/08 21:31:45
@Author  : pengyuan.li
@File    : 0x24-addtionChains.py
@Software: VSCode
'''

# here put the import lib


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


if __name__ == "__main__":
    nums = [5, 7, 12, 15, 77]
    addc = addChains()
    for i in nums:
        
        addc.printChains(i)