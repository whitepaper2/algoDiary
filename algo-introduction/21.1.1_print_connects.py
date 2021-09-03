#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm


class UnionFindSets:
    def __init__(self, A):
        """
        维护父节点(字典)、高度(字典)、并查集个数
        :param A: 输入list
        """
        self.parent = {}
        self.setsNum = len(A)
        self.rank = {}
        for a in A:
            self.parent[a] = a
            self.rank[a] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xHead = self.find(x)
        yHead = self.find(y)
        if xHead == yHead:
            return
        # 若改成 >= , 结果不一致？？？
        if self.rank[xHead] > self.rank[yHead]:
            self.parent[yHead] = xHead
        else:
            self.parent[xHead] = yHead
            if self.rank[xHead] == self.rank[yHead]:
                self.rank[yHead] += 1
        self.setsNum -= 1

    def isSameSet(self, u, v):
        if self.find(u) == self.find(v):
            return True
        else:
            return False


def connectComponents(vertex, edge):
    from collections import defaultdict

    ufs = UnionFindSets(vertex)
    for u, v in edge:
        if ufs.find(u) != ufs.find(v):
            ufs.union(u, v)
    connects = defaultdict(set)
    for k, v in ufs.parent.items():
        connects[v].add(k)
    return [v for k, v in connects.items()]


class UnionFindSets2:
    """
    note:不使用压缩方式的，还没实现
    """
    def __init__(self, A):
        """
        维护父节点(字典)、高度(字典)、并查集个数
        :param A: 输入list
        """
        self.symbol = dict()
        self.setsNum = len(A)
        for a in A:
            self.symbol[a] = a

    def find(self, x):
        while x != self.symbol[x]:
            x = self.symbol[x]
        return x

    def union(self, x, y):
        xHead = self.find(x)
        yHead = self.find(y)
        self.symbol[xHead] = yHead
        self.setsNum -= 1

    def isSameSet(self, u, v):
        if self.find(u) == self.find(v):
            return True
        else:
            return False


def connectComponents2(vertex, edge):
    from collections import defaultdict

    ufs = UnionFindSets2(vertex)
    for u, v in edge:
        if ufs.find(u) != ufs.find(v):
            ufs.union(u, v)
    connects = defaultdict(set)
    for k, v in ufs.symbol.items():
        connects[v].add(k)
    return [v for k, v in connects.items()]


if __name__ == "__main__":
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    edge = [['d', 'i'], ['f', 'k'], ['g', 'i'], ['b', 'g'], ['a', 'h'], ['i', 'j'], ['d', 'k'], ['b', 'j'], ['d', 'f'],
            ['g', 'j'], ['a', 'e']]
    res = connectComponents(vertex, edge)
    print(res)
    res = connectComponents2(vertex, edge)
    print(res)
    ufs = UnionFindSets2(vertex)
    for u, v in edge:
        ufs.union(u, v)
    print(ufs.symbol)
