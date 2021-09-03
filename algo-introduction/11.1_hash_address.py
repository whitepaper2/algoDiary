#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 下午3:27
# @Author  : pengyuan.li
# @Site    : 
# @File    : 11.1_hash_address.py
# @Software: PyCharm

# 散列函数：除法散列法、乘法散列法、全域散列法
# 散列表的冲突解决方法：1.拉链法；2.开放寻址法；3.再散列
# 其中开放寻址法包括线性探查、二次探查、双重散列


class OpenAddressHash(object):
    def __init__(self, size):
        self.T = [None] * size
        self.size = size

    def double_hash(self, k, i):
        h1 = k % self.size
        h2 = 1 + k % (self.size - 2)
        return (h1 + i * h2) % self.size

    def linear_hash(self, k, i):
        h1 = k % self.size
        return (h1 + i) % self.size

    def quard_hash(self, k, i):
        h1 = k % self.size
        c1, c2 = 2, 3
        return (h1 + c1 * i + c2 * i * i) % self.size

    def hash_insert(self, k):
        i = 0
        while i < self.size:
            j = self.double_hash(k, i)
            # j = self.linear_hash(k, i)
            # j = self.quard_hash(k, i)
            if not self.T[j]:
                self.T[j] = k
                return j
            i += 1
        return "hash table overflow!"

    def hash_search(self, k):
        i = 0
        j = self.double_hash(k, i)
        while self.T[j] and i < self.size:
            j = self.double_hash(k, i)
            # j = self.linear_hash(k, i)
            # j = self.quard_hash(k, i)
            if self.T[j] == k:
                return j
            i += 1
        return None


if __name__ == "__main__":
    keys = [79, 69, 98, 72, 14, 50]
    example = OpenAddressHash(13)
    for k in keys:
        print(example.hash_insert(k))
    for k in [79, 98, 14, 400, 39]:
        print(example.hash_search(k))
