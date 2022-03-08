#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    :
# @File    : 21.1_union_sets.py
# @Software: PyCharm

from collections import defaultdict


class UnionFindSets:

    def __init__(self, A):
        """
        维护父节点(字典)、高度(字典)、并查集个数
        :param A: 输入list
        """
        self.parent = {}
        self.rank = {}
        self.setsNum = len(A)
        self.sets = defaultdict(set)
        for a in A:
            self.parent[a] = a
            self.rank[a] = 1
            self.sets[a].add(a)

    def find(self, x):
        # while x != self.parent[x]:
        #     x = self.parent[x]
        # return self.parent[x]
        father = self.parent[x]
        if father != x:
            father = self.find(father)
        self.parent[x] = father
        return father

    def union(self, x, y):
        if not x or not y:
            return
        xHead = self.find(x)
        yHead = self.find(y)
        if xHead == yHead:
            return

        xRank = self.rank[xHead]
        yRank = self.rank[yHead]
        # if xRank >= yRank:
        #     self.parent[yHead] = xHead
        #     if xRank == yRank:
        #         self.rank[xRank] += 1
        # else:
        #     self.parent[xHead] = yHead
        if xRank < yRank:
            self.parent[xHead] = yHead
            self.sets[xHead].add(yHead)
        else:
            self.parent[yHead] = xHead
            self.sets[yHead].add(xHead)
            if xRank == yRank:
                self.rank[xHead] += 1
        self.setsNum -= 1

    def printSets(self, x):
        """
        打印x所在的集合元素
        :param x:
        :return:
        """
        print(self.sets[x])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    ufs = UnionFindSets(nums)
    ufs.union(1, 3)
    print(ufs.parent, ufs.rank, ufs.setsNum)
    ufs.printSets(3)

    ufs.union(1, 3)
    print(ufs.parent, ufs.rank, ufs.setsNum)
