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


class ChainedHash(object):
    def __init__(self, size):
        self.T = [None] * size
        self.size = size

    def divide_hash(self, k):
        return k % self.size

    def hash_insert(self, k):
        i = self.divide_hash(k)
        if self.T[i]:
            self.T[i].append(k)
        else:
            self.T[i] = [k]
        return "position={}".format(i)

    def hash_search(self, k):
        i = self.divide_hash(k)
        if i and self.T[i]:
            for ik in self.T[i]:
                if ik == k:
                    return i
        else:
            return None


if __name__ == "__main__":
    keys = [79, 69, 98, 72, 14, 50]
    example = ChainedHash(13)
    for k in keys:
        print(example.hash_insert(k))
    for k in [79, 98, 14, 400, 39]:
        print(example.hash_search(k))
